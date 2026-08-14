#!/usr/bin/env python3

from display import choose_location,display_weather

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

def test_choose_multiple_locations(monkeypatch):
    locations = [
        {
            "name": "Pune",
            "state": "Maharashtra",
            "country": "IN",
            "lat": 18.52,
            "lon": 73.85
        },
        {
            "name": "Pune",
            "state": "Colorado",
            "country": "US",
            "lat": 37.77,
            "lon": -104.65
        }
    ]

    monkeypatch.setattr("builtins.input", lambda _: "2")
    """basically tells the test: Whenever the code calls input(), pretend the user entered 2."""

    lat, lon = choose_location(locations)

    assert lat == 37.77
    assert lon == -104.65

def test_choose_location_invalid_input(monkeypatch):
    locations = [
        {
            "name": "Pune",
            "state": "Maharashtra",
            "country": "IN",
            "lat": 18.52,
            "lon": 73.85
        },
        {
            "name": "Pune",
            "state": "Colorado",
            "country": "US",
            "lat": 37.77,
            "lon": -104.65
        }
    ]

    inputs = iter(["abc", "1"])
    """ 
        We're telling the test that there will be two inputs:
        first → abc  
        second → 1

        then:
        lambda _: next(inputs)
        makes input return them one after another    
    """
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    lat, lon = choose_location(locations)

    assert lat == 18.52
    assert lon == 73.85

def test_choose_location_invalid_choice(monkeypatch):
    locations = [
        {
            "name": "Pune",
            "state": "Maharashtra",
            "country": "IN",
            "lat": 18.52,
            "lon": 73.85
        },
        {
            "name": "Pune",
            "state": "Colorado",
            "country": "US",
            "lat": 37.77,
            "lon": -104.65
        }
    ]

    inputs = iter(["5", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    lat, lon = choose_location(locations)

    assert lat == 18.52
    assert lon == 73.85

def test_display_weather(capsys):
    data = {
        "name": "Pune",
        "main": {
            "temp": 25,
            "humidity": 70,
            "pressure": 1012
        },
        "weather": [
            {
                "description": "clear sky"
            }
        ],
        "wind": {
            "speed": 3.5
        }
    }

    display_weather(data)

    captured = capsys.readouterr()

    assert "City: Pune" in captured.out
    assert "Temperature: 25" in captured.out
    assert "Humidity: 70" in captured.out
    assert "Pressure: 1012" in captured.out
    assert "Weather: clear sky" in captured.out
    assert "Wind Speed: 3.5" in captured.out
