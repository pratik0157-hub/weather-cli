# Weather CLI Requirements

## Goal

Build a simple command-line application that lets a user check the current weather of any city.

The project is mainly for learning APIs, argparse, project organization and software engineering basics.

---

# Functional Requirements

## FR-1

The user should be able to enter a city name from the command line.

Example

```
python3 main.py Pune
```

---

## FR-2

The application should convert the city name into latitude and longitude using the OpenWeather Geocoding API.

---

## FR-3

If multiple matching cities are found, the application should display them and allow the user to choose one.

---

## FR-4

The application should retrieve the current weather using the selected coordinates.

---

## FR-5

The application should display

- City Name
- Temperature
- Feels Like
- Humidity
- Wind Speed
- Weather Description

---

## FR-6

The application should display a clear error if

- Internet connection fails
- API request fails
- City is not found
- Invalid input is given

---

# Non-Functional Requirements

## NFR-1

The application should be easy to use.

---

## NFR-2

The code should be modular and easy to understand.

---

## NFR-3

The project should work on Linux, Windows and macOS.

---

## NFR-4

Sensitive information like API keys should not be stored directly in the source code.

---

## NFR-5

The project should follow a clean folder structure.

---

# Project Scope

Included

- Current weather
- Geocoding
- argparse
- Multiple location selection
- Error handling

Not Included

- Weather forecast
- Weather maps
- Air pollution
- Weather history
- GUI
- Mobile application

---

# APIs Used

## OpenWeather Geocoding API

Purpose

Convert city names into latitude and longitude.

---

## OpenWeather Current Weather API

Purpose

Retrieve the current weather using latitude and longitude.

---

# Success Criteria

The project is considered complete if:

- The user can enter a city.
- The correct weather is displayed.
- Errors are handled properly.
- The project has documentation.
- The project is organized into modules.