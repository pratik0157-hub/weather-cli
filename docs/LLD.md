# Low Level Design (LLD)

# Project Structure

```
weather-cli/
│
├── main.py
├── cli.py
├── geocode.py
├── weather.py
├── display.py
├── config.py
│
├── docs/
│   ├── HLD.md
│   ├── LLD.md
│   └── requirements.md
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Module Responsibilities

## main.py

Acts as the controller of the application.

Responsibilities

- Start the program
- Call all required modules
- Control program flow

Flow

```
main()

│

├── parse_arguments()

├── get_coordinates()

├── choose_location() (if needed)

├── get_weather()

└── show_weather()
```

---

## cli.py

Responsible for handling command-line arguments.

Functions

```
parse_arguments()
```

Returns

```
args.city
```

---

## geocode.py

Responsible for communicating with the Geocoding API.

Functions

```
get_coordinates(city)
```

Input

```
City Name
```

Returns

```
[
    {
        "name": "...",
        "lat": ...,
        "lon": ...
    }
]
```

---

## weather.py

Responsible for communicating with the Current Weather API.

Functions

```
get_weather(lat, lon)
```

Input

```
Latitude
Longitude
```

Returns

```
Weather JSON
```

---

## display.py

Responsible for formatting and displaying information.

Functions

```
show_weather(weather)
```

Displays

- City
- Temperature
- Feels Like
- Humidity
- Wind Speed
- Description

---

## config.py

Stores project constants.

Examples

```
API_KEY
BASE_GEOCODE_URL
BASE_WEATHER_URL
```

---

# Data Flow

```
User

│

▼

CLI

│

▼

parse_arguments()

│

▼

City Name

│

▼

get_coordinates()

│

▼

Latitude + Longitude

│

▼

get_weather()

│

▼

Weather JSON

│

▼

show_weather()

│

▼

Terminal Output
```

---

# Error Handling

Possible Errors

- No internet connection
- Invalid API key
- City not found
- API request failed
- Invalid user selection

The application displays a meaningful error message and exits gracefully.

---

# APIs Used

## Geocoding API

Input

```
City Name
```

Output

```
Latitude
Longitude
```

---

## Current Weather API

Input

```
Latitude
Longitude
```

Output

```
Temperature
Humidity
Wind Speed
Weather Description
```

---

# Design Principles

- Each module has a single responsibility.
- Functions return data instead of printing whenever possible.
- API communication is separated from presentation.
- The application flow is controlled only by `main.py`.