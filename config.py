#!/usr/bin/env python3

from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Get the API key from the environment variables
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set")

# Base URL for converting a city name to coordinates
GEOCODE_URL = "http://api.openweathermap.org/geo/1.0/direct"

# Base URL for fetching weather data using coordinates
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"