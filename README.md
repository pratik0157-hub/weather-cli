# Weather CLI

[![Python CI](https://github.com/pratik0157-hub/weather-cli/actions/workflows/python.yml/badge.svg)](https://github.com/pratik0157-hub/weather-cli/actions/workflows/python.yml)

A simple command-line weather application built in Python.

The user enters a city name, the program finds its latitude and longitude using the OpenWeather Geocoding API, then fetches the current weather using the OpenWeather Weather API.

> This project was built as part of my journey to learn Python and software engineering by building real applications instead of only solving coding problems.

This project was built to practice:

- Python modules
- argparse
- Working with REST APIs
- JSON
- Project organization
- Error handling
- Software engineering basics

---

## Features

- Search weather by city name
- Automatically convert city name to latitude & longitude
- Handles multiple matching locations
- Shows:
  - Temperature
  - Feels Like
  - Humidity
  - Wind Speed
  - Weather Description
- Friendly error messages
- Command-line interface using argparse

---

## Technologies Used

- Python 3
- argparse
- requests
- OpenWeather Geocoding API
- OpenWeather Current Weather API

---

## Project Structure

```
weather-cli/
│
├── main.py          # Controls the flow of the program
├── cli.py           # Handles command-line arguments
├── geocode.py       # Gets latitude & longitude
├── weather.py       # Fetches weather data
├── display.py       # Prints formatted output
├── config.py        # Stores constants
│
├── .github/
│   └── workflows/
│       └── python.yml
│
│
├── docs/
│   ├── requirements.md
│   ├── HLD.md
│   └── LLD.md
│
├── tests/
│   ├── test_cli.py
│   └── test_display.py
│    
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd weather-cli
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it

Linux/macOS

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```
OPENWEATHER_API_KEY=your_api_key_here
```

---

## Usage

```bash
python3 main.py Pune
```

Example

```
City: Pune

Temperature : 28°C
Feels Like  : 30°C
Humidity    : 74%
Wind Speed  : 3.5 m/s
Weather     : Broken Clouds
```

## Testing

This project uses **pytest** for testing.

Run the test suite from the project root:

```bash
python3 -m pytest
```

The tests currently cover:

- CLI argument parsing
- Location selection 
- for weather info and geocode test manually


## Continuous Integration

GitHub Actions automatically runs the test suite on every push and pull request.

This ensures that future changes do not break existing functionality.

---

## What I Learned

While building this project I learned:

- Making HTTP requests
- Parsing JSON responses
- Using argparse
- Splitting code into modules
- Organizing a Python project
- Handling API errors
- Writing cleaner code

---

## Future Improvements

- Colored terminal output
- Weather icons
- Unit conversion
- Save recent searches
- Package as an installable CLI

---

## License

MIT License