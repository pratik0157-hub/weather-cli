#!/usr/bin/env python3

import requests
from config import API_KEY, GEOCODE_URL

def get_coordinates(city):
    # Create the API URL using the city name and API key
    url = f"{GEOCODE_URL}?q={city}&limit=5&appid={API_KEY}"

    # Send a GET request to the geocoding API
    """response = requests.get(url)

    print("GEOCODE STATUS:", response.status_code)
    print("GEOCODE RESPONSE:", response.text)

    if response.status_code == 200:
        return response.json()
    else:
        return []"""
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the JSON response into a Python object
        coordinates = response.json()
        return coordinates
    else:
        # Return None if the request fails
        return None