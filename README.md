# Temperature Forecasts

The api `/v1/forcast/get_coolest_10_districts` list of districts with their name in english and bengali.
---

## Detailed Setup Instructions

Below are the detailed commands you will need to execute to set up and run the application. These steps cover environment setup, dependency installation, database migrations, and running the application.

### Create Virtual Environment

Create virtual environment using python 3.10.

```bash
python3 -m venv venv
```

### Activating the Virtual Environment

Activate your previously created virtual environment using the following command:

```bash
source venv/bin/activate
```

This command activates the virtual environment.

### Installing Dependencies

Once your environment is activated, install all required Python dependencies listed in the `requirements.txt` file:

```bash
# Install project dependencies
pip install -r requirements.txt
```

This command reads the `requirements.txt` file in your project directory and installs all the listed packages. This file includes FastAPI, Uvicorn for running the server, and other necessary libraries.

### Update environment variables

To run fastapi on the server, please configure 
environment variables properly by following the commands. Default values
are already urls replace f you want to use different urls.

```bash
cp example.env .env
```

```bash
SECRET_KEY= Put your app secret key here
DISTRICT_DATA_URL=https://raw.githubusercontent.com/strativ-dev/technical-screening-test/main/bd-districts.json
FORCAST_URL=https://api.open-meteo.com/v1/forecast
```

### Running the Application

Finally, start your FastAPI application by running the Python script that contains your FastAPI app instance:

```bash

python main.py
```

This command will start the server, making your application accessible on the configured port (usually http://localhost:8000).

