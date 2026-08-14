#!/usr/bin/env python3

from unittest.mock import patch
from forecast import get_forecast_info, get_forecast_summary


@patch("forecast.requests.get")
def test_get_forecast_info_success(mock_get):
    mock_data = {
        "cod": "200",
        "message": 0,
        "cnt": 4,
        "list": [
            {
                "dt": 1755158400,
                "main": {
                    "temp": 27.5,
                    "feels_like": 28.1,
                    "temp_min": 26.8,
                    "temp_max": 28.2,
                    "humidity": 78
                },
                "weather": [
                    {
                        "main": "Rain",
                        "description": "light rain"
                    }
                ],
                "pop": 0.85
            },
            {
                "dt": 1755169200,
                "main": {
                    "temp": 26.2,
                    "feels_like": 26.8,
                    "temp_min": 25.9,
                    "temp_max": 26.5,
                    "humidity": 82
                },
                "weather": [
                    {
                        "main": "Rain",
                        "description": "moderate rain"
                    }
                ],
                "pop": 0.90
            },
            {
                "dt": 1755180000,
                "main": {
                    "temp": 25.4,
                    "feels_like": 26.0,
                    "temp_min": 25.0,
                    "temp_max": 25.8,
                    "humidity": 85
                },
                "weather": [
                    {
                        "main": "Clouds",
                        "description": "broken clouds"
                    }
                ],
                "pop": 0.40
            },
            {
                "dt": 1755190800,
                "main": {
                    "temp": 24.8,
                    "feels_like": 25.2,
                    "temp_min": 24.5,
                    "temp_max": 25.0,
                    "humidity": 88
                },
                "weather": [
                    {
                        "main": "Rain",
                        "description": "heavy intensity rain"
                    }
                ],
                "pop": 0.95
            }
        ],
        "city": {
            "name": "Pune",
            "country": "IN"
        }
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_data

    result = get_forecast_info(18.52, 73.85)

    assert result == mock_data


@patch("forecast.requests.get")
def test_get_forecast_info_failure(mock_get):
    mock_get.return_value.status_code = 404

    result = get_forecast_info(18.52, 73.85)

    assert result is None


def test_get_forecast_summary_success():
    mock_data = {
        "list": [
            {
                "dt_txt": "2026-08-14 09:00:00",
                "main": {"temp": 27.5},
                "weather": [{"description": "light rain"}]
            },
            {
                "dt_txt": "2026-08-14 12:00:00",
                "main": {"temp": 30.2},
                "weather": [{"description": "light rain"}]
            },
            {
                "dt_txt": "2026-08-14 15:00:00",
                "main": {"temp": 28.4},
                "weather": [{"description": "broken clouds"}]
            },
            {
                "dt_txt": "2026-08-14 18:00:00",
                "main": {"temp": 25.8},
                "weather": [{"description": "light rain"}]
            }
        ]
    }

    result = get_forecast_summary(mock_data)

    assert result == {
        "2026-08-14": {
            "max_temp": 30.2,
            "min_temp": 25.8,
            "description": "light rain"
        }
    }


def test_get_forecast_summary_empty():
    mock_data = {
        "list": []
    }

    result = get_forecast_summary(mock_data)

    assert result == {}