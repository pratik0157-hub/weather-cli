#!/usr/bin/env python3

from cli import parse_arguments
from geocode import get_coordinates
from weather import get_weather
from display import choose_location, display_weather, display_json, display_forecast
from forecast import get_forecast_info, get_forecast_summary


def main():
    args = parse_arguments()

    locations = get_coordinates(args.city)
    
    """print("LOCATIONS:", locations)

    if not locations:
        print("Invalid input. Please try again.")
        return

    lat, lon = choose_location(locations)
    print("COORDINATES:", lat, lon)

    if args.forecast:
        info = get_forecast_info(lat, lon)
        print("FORECAST RESPONSE:", info)

        summary = get_forecast_summary(info)
        print("FORECAST SUMMARY:", summary)

        display_forecast(summary)"""

    if not locations:
        print("Invalid input. Please try again.")
        return

    lat, lon = choose_location(locations)

    weather = get_weather(lat, lon)

    if not weather:
        print("Unable to fetch weather data. Please try again.")
        return
    
    if args.forecast:
            info = get_forecast_info(lat,lon)
            summary = get_forecast_summary(info)
            display_forecast(summary)

    if args.json:
        print(display_json(weather))
        return

    display_weather(weather)


if __name__ == "__main__":
    main()