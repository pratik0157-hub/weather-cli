#!/usr/bin/env python3
import json


def choose_location(geo_pos):
    # Check if the API returned more than one matching location
    if len(geo_pos) > 1:
        print("Multiple locations found:")

        # Display all matching locations with a number
        for i in range(len(geo_pos)):
            city = geo_pos[i]
            print(f"{i + 1}. {city['name']}, {city['state']}, {city['country']}")

        # Let the user choose the correct location
        num = 0
        while num not in range(1, len(geo_pos)+1):
            try:
                num = int(input("Enter the correct choice: "))
            except ValueError:
                print("Invalid input. Please enter a integer number.")
            else:
                if num in range(1,len(geo_pos)+1):
                    final_city = geo_pos[num - 1]
                    break
                else:
                    print(f"Invalid choice. Enter a number between 1 and {len(geo_pos)}.")

    else:
        # If there is only one match, select it directly
        final_city = geo_pos[0]

    # Extract the latitude and longitude of the selected location
    lat = final_city["lat"]
    lon = final_city["lon"]

    return lat, lon


def weather_info(data):
    # Display the weather information in a readable format
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"])
    print("Humidity:", data["main"]["humidity"])
    print("Pressure:", data["main"]["pressure"])
    print("Weather:", data["weather"][0]["description"])
    print("Wind Speed:", data["wind"]["speed"])


def display_json(info):
    return json.dumps(info, indent=4)