#!/usr/bin/env python3

from cli import parse_arguments
from geocode import get_coordinates
from weather import get_weather
from display import choose_location, weather_info, display_json


def main():
    args = parse_arguments()

    locations = get_coordinates(args.city)

    if not locations:
        print("Invalid input. Please try again.")
        return

    lat, lon = choose_location(locations)

    weather = get_weather(lat, lon)

    if not weather:
        print("Unable to fetch weather data. Please try again.")
        return

    if args.json:
        print(display_json(weather))
        return

    weather_info(weather)


if __name__ == "__main__":
    main()