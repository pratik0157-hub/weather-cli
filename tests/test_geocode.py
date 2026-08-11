#!/usr/bin/env python3

from unittest.mock import patch
from geocode import get_coordinates


@patch("geocode.requests.get")
def test_get_coordinates_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {
            "name": "Pune",
            "lat": 18.52,
            "lon": 73.85
        }
    ]

    result = get_coordinates("Pune")

    assert result == [
        {
            "name": "Pune",
            "lat": 18.52,
            "lon": 73.85
        }
    ]

@patch("geocode.requests.get")
def test_get_coordinates_failure(mock_get):
    mock_get.return_value.status_code = 404

    result = get_coordinates("Pune")

    assert result is None