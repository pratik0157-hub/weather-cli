#!/usr/bin/env python3

from unittest.mock import patch
from weather import get_weather


@patch("weather.requests.get")
def test_get_weather_success(mock_get):
    mock_data = {
        "coord": {
            "lon": 73.8567,
            "lat": 18.5204
        },
        "weather": [
            {
                "id": 800,
                "main": "Clear",
                "description": "clear sky",
                "icon": "01d"
            }
        ],
        "main": {
            "temp": 28.5,
            "feels_like": 29.1,
            "temp_min": 27.2,
            "temp_max": 30.4,
            "pressure": 1008,
            "humidity": 61
        },
        "visibility": 10000,
        "wind": {
            "speed": 3.6,
            "deg": 250
        },
        "clouds": {
            "all": 10
        },
        "name": "Pune"
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_data

    result = get_weather(18.52, 73.85)

    assert result == mock_data


@patch("weather.requests.get")
def test_get_weather_failure(mock_get):
    mock_get.return_value.status_code = 404

    result = get_weather(18.52, 73.85)

    assert result is None