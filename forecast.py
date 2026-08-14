#!/usr/bin/env python3

import requests
from config import API_KEY, FORECAST_URL
from collections import Counter


def get_forecast_info(lat, lon):
    # Create the API URL using the latitude, longitude, and API key
    url = f"{FORECAST_URL}?lat={lat}&lon={lon}&cnt=40&units=metric&appid={API_KEY}"

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


def get_forecast_summary(data):
    daily_forecast = {}
    for forecast in data["list"]:
            date = forecast["dt_txt"].split()[0]
            temperature = forecast["main"]["temp"]
            description = forecast["weather"][0]["description"]
            if date not in daily_forecast:
                daily_forecast[date] = []
            daily_forecast[date].append({
                "temperature": temperature,
                "description": description
            })
    daily_summary = {}

    for date, forecast_list in daily_forecast.items():
        if forecast_list:
            # Get the full dictionary entry of the highest temperature
            max_entry = max(forecast_list, key=lambda x: x["temperature"])
            min_entry = min(forecast_list,key=lambda x: x["temperature"])
            descriptions = [
                forecast["description"]
                for forecast in forecast_list
            ]
            most_common = Counter(descriptions).most_common(1)[0][0]
            daily_summary[date] = {
                "max_temp": max_entry["temperature"],
                "min_temp": min_entry["temperature"],
                "description": most_common 
            }

    return daily_summary
            