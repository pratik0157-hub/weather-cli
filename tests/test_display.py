#!/usr/bin/env python3

from display import choose_location

def test_choose_single_location():
    locations = [
        {
            "name": "Pune",
            "lat": 18.52,
            "lon": 73.85
        }
    ]

    lat, lon = choose_location(locations)

    assert lat == 18.52
    assert lon == 73.85
