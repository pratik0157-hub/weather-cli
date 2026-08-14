#!/usr/bin/env python3


from unittest.mock import patch
from main import main


@patch("main.display_weather")
@patch("main.get_weather")
@patch("main.choose_location")
@patch("main.get_coordinates")
@patch("main.parse_arguments")
def test_main_displays_weather(
    mock_parse,
    mock_coordinates,
    mock_choose,
    mock_weather,
    mock_display
):
    mock_parse.return_value.city = "Pune"
    mock_parse.return_value.forecast = False
    mock_parse.return_value.json = False

    mock_coordinates.return_value = [
        {
            "name": "Pune",
            "lat": 18.52,
            "lon": 73.85
        }
    ]

    mock_choose.return_value = (18.52, 73.85)

    mock_weather.return_value = {
        "name": "Pune",
        "main": {
            "temp": 25,
            "humidity": 70,
            "pressure": 1012
        },
        "weather": [
            {"description": "clear sky"}
        ],
        "wind": {
            "speed": 3.5
        }
    }

    main()

    mock_display.assert_called_once_with(mock_weather.return_value)


@patch("main.get_coordinates")
@patch("main.parse_arguments")
def test_main_no_locations(mock_parse, mock_coordinates, capsys):
    mock_parse.return_value.city = "InvalidCity"
    mock_parse.return_value.forecast = False
    mock_parse.return_value.json = False

    mock_coordinates.return_value = []

    main()

    captured = capsys.readouterr()

    assert "Invalid input. Please try again." in captured.out


@patch("main.get_weather")
@patch("main.choose_location")
@patch("main.get_coordinates")
@patch("main.parse_arguments")
def test_main_weather_failure(
    mock_parse,
    mock_coordinates,
    mock_choose,
    mock_weather,
    capsys
):
    mock_parse.return_value.city = "Pune"
    mock_parse.return_value.forecast = False
    mock_parse.return_value.json = False

    mock_coordinates.return_value = [
        {
            "name": "Pune",
            "lat": 18.52,
            "lon": 73.85
        }
    ]

    mock_choose.return_value = (18.52, 73.85)
    mock_weather.return_value = None

    main()

    captured = capsys.readouterr()

    assert "Unable to fetch weather data. Please try again." in captured.out

@patch("main.display_json")
@patch("main.get_weather")
@patch("main.choose_location")
@patch("main.get_coordinates")
@patch("main.parse_arguments")
def test_main_json_output(
    mock_parse,
    mock_coordinates,
    mock_choose,
    mock_weather,
    mock_display_json,
    capsys
):
    mock_parse.return_value.city = "Pune"
    mock_parse.return_value.forecast = False
    mock_parse.return_value.json = True

    mock_coordinates.return_value = [
        {
            "name": "Pune",
            "lat": 18.52,
            "lon": 73.85
        }
    ]

    mock_choose.return_value = (18.52, 73.85)

    weather = {
        "name": "Pune",
        "main": {
            "temp": 25
        }
    }

    mock_weather.return_value = weather
    mock_display_json.return_value = '{"name": "Pune"}'

    main()

    mock_display_json.assert_called_once_with(weather)

    captured = capsys.readouterr()
    assert '{"name": "Pune"}' in captured.out

@patch("main.display_weather")
@patch("main.display_forecast")
@patch("main.get_forecast_summary")
@patch("main.get_forecast_info")
@patch("main.get_weather")
@patch("main.choose_location")
@patch("main.get_coordinates")
@patch("main.parse_arguments")
def test_main_forecast(
    mock_parse,
    mock_coordinates,
    mock_choose,
    mock_weather,
    mock_forecast_info,
    mock_forecast_summary,
    mock_display_forecast,
    mock_display_weather
):
    mock_parse.return_value.city = "Pune"
    mock_parse.return_value.forecast = True
    mock_parse.return_value.json = False

    mock_coordinates.return_value = [
        {
            "name": "Pune",
            "lat": 18.52,
            "lon": 73.85
        }
    ]

    mock_choose.return_value = (18.52, 73.85)

    mock_weather.return_value = {
        "name": "Pune",
        "main": {
            "temp": 25,
            "humidity": 70,
            "pressure": 1012
        },
        "weather": [
            {"description": "clear sky"}
        ],
        "wind": {
            "speed": 3.5
        }
    }

    mock_forecast_info.return_value = {
        "2026-08-14": {
            "max_temp": 30,
            "min_temp": 24,
            "description": "clear sky"
        }
    }

    mock_forecast_summary.return_value = {
        "2026-08-14": {
            "max_temp": 30,
            "min_temp": 24,
            "description": "clear sky"
        }
    }

    main()

    mock_forecast_info.assert_called_once_with(18.52, 73.85)
    mock_forecast_summary.assert_called_once_with(
        mock_forecast_info.return_value
    )
    mock_display_forecast.assert_called_once_with(
        mock_forecast_summary.return_value
    )