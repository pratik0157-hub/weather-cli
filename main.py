#!/usr/bin/env python3

# Import functions from different modules
from cli import parse_arguments
from geocode import get_coordinates
from weather import get_weather
from display import choose_location, weather_info

# Get the city name entered by the user from the command line
city_name = parse_arguments()

# Use the city name to get matching locations and their coordinates
locations = get_coordinates(city_name)

# Check if any locations were found
if locations:
    # If multiple locations exist, let the user choose one
    lat, lon = choose_location(locations)

    # Fetch weather data using the selected latitude and longitude
    weather = get_weather(lat, lon)

    # Check if the weather data was fetched successfully
    if weather:
        # Display the weather information in a readable format
        weather_info(weather)
    else:
        # Weather API request failed
        print("Invalid input. Please try again.")
else:
    # No matching city was found
    print("Invalid input. Please try again.")