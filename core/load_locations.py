from datetime import date, timedelta

import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

from core.config import district_information, config


class WeatherForecasts:

    def __init__(self):
        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        self._open_meteo = openmeteo_requests.Client(session=retry_session)
        self._coolest_10_districts = pd.DataFrame()

    def get_coolest_10_districts(self):
        return self._coolest_10_districts[["district", "bn_name"]].to_dict('records')

    def preload_weather_forecast(self, locations: list = district_information["districts"]):
        params = {
            "latitude": 52.52,
            "longitude": 13.41,
            "hourly": "temperature_2m",
            "timezone": "Asia/Dacca",
            "start_date": date.today(),
            "end_date": date.today() + timedelta(days=7)
        }
        for district in locations:
            params["latitude"] = district["lat"]
            params["longitude"] = district["long"]
            responses = self._open_meteo.weather_api(config.FORCAST_URL, params=params)
            hourly = responses[0].Hourly()
            hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
            hourly_data = {"date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            ), "temperature": hourly_temperature_2m}

            hourly_dataframe = pd.DataFrame(data=hourly_data)
            h = hourly_dataframe['date'].dt.hour
            hourly_dataframe = hourly_dataframe[h.eq(14)]

            average_temp = hourly_dataframe["temperature"].mean()
            if not self._coolest_10_districts.empty:
                hourly_dataframe = pd.concat([
                    self._coolest_10_districts,
                    pd.DataFrame(data={
                        "district": district["name"],
                        "bn_name": district["bn_name"],
                        "average_temperature": average_temp
                    }, index=[0])])

                self._coolest_10_districts = hourly_dataframe.sort_values(
                    by=["average_temperature"], ascending=True).reset_index(drop=True).head(10)
            else:
                self._coolest_10_districts = pd.DataFrame(data={
                        "district": district["name"],
                        "bn_name": district["bn_name"],
                        "average_temperature": average_temp
                    }, index=[0])

    def reload_weather_forecast(self):
        print("Reloading weather")
        self._coolest_10_districts = pd.DataFrame()
        self.preload_weather_forecast()


weather_forecasts = WeatherForecasts()
