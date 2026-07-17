#!/usr/bin/env python3

def choose_location(geo_pos):
    # Check if the API returned more than one matching location
    if len(geo_pos) > 1:
        print("Multiple locations found:")

        # Display all matching locations with a number
        for i in range(len(geo_pos)):
            city = geo_pos[i]
            print(f"{i + 1}. {city['name']}, {city['state']}, {city['country']}")

        # Let the user choose the correct location
        num = int(input("Enter the correct choice: "))
        final_city = geo_pos[num - 1]

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