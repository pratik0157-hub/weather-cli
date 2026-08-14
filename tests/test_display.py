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
