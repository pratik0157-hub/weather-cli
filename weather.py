#!/usr/bin/env python3

import requests
from config import API_KEY, WEATHER_URL

def get_weather(lat, lon):
    # Create the API URL using the latitude, longitude, and API key
    url = f"{WEATHER_URL}?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"

    # Send a GET request to the weather API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the JSON response into a Python object
        info = response.json()
        return info
    else:
        # Return None if the request fails
        return None