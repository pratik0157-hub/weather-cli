# High Level Design (HLD)

# Weather CLI

## Goal

The application allows the user to enter a city name from the command line, retrieves its coordinates using the OpenWeather Geocoding API, fetches the current weather using the OpenWeather Weather API, and displays the result.

---

# High Level Flow

```
                User
                  │
                  ▼
          Command Line (CLI)
                  │
                  ▼
          Argument Parser
                  │
                  ▼
         Geocoding Module
                  │
      (Latitude & Longitude)
                  │
                  ▼
          Weather Module
                  │
        (Weather Information)
                  │
                  ▼
          Display Module
                  │
                  ▼
               Terminal
```

---

# Components

## CLI

Accepts user input from the command line.

Input

- City Name

Output

- Parsed command-line arguments

---

## Geocoding Module

Uses the OpenWeather Geocoding API to convert the city name into latitude and longitude.

Input

- City Name

Output

- Latitude
- Longitude

---

## Weather Module

Uses the latitude and longitude to retrieve the current weather.

Input

- Latitude
- Longitude

Output

- Weather Data

---

## Display Module

Formats and prints the weather information in a readable format.

Output

- Temperature
- Feels Like
- Humidity
- Wind Speed
- Weather Description

---

# External Services

## OpenWeather Geocoding API

Converts city names into coordinates.

---

## OpenWeather Current Weather API

Returns weather information for the given coordinates.

---

# Overall Workflow

1. User enters a city name.
2. argparse reads the command-line argument.
3. The Geocoding API returns matching locations.
4. If multiple locations exist, the user selects one.
5. The Weather API is called using the selected coordinates.
6. Weather information is displayed.