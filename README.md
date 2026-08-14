# Weather CLI

[![Python CI](https://github.com/pratik0157-hub/weather-cli/actions/workflows/python.yml/badge.svg)](https://github.com/pratik0157-hub/weather-cli/actions/workflows/python.yml)

[![codecov](https://codecov.io/gh/pratik0157-hub/weather-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/pratik0157-hub/weather-cli)


A modular command-line weather application built with Python and the OpenWeather APIs.

The application accepts a city name, converts it into geographic coordinates using the OpenWeather Geocoding API, and retrieves current weather information and forecast data. Forecast data is processed into daily summaries containing minimum temperature, maximum temperature, and the most common weather condition.

This project started as a simple Python weather application and is being developed incrementally to practice real-world software engineering practices.

---

## Project Highlights

* Modular Python project structure
* REST API integration using `requests`
* Command-line interface using `argparse`
* City geocoding and multiple-location selection
* Current weather and forecast functionality
* Daily forecast data processing
* Automated testing with `pytest`
* External API mocking with `unittest.mock`
* API success and failure testing
* GitHub Actions CI
* Multi-platform CI testing
* Multiple Python versions tested through a matrix
* Dependency caching in CI
* Dependabot dependency updates
* Feature branches and Pull Requests
* Environment variables for API credentials

---

## Features

* Search weather by city name
* Required `--city` / `-c` command-line option
* City option can be placed anywhere in the command
* Convert city names into latitude and longitude
* Handle multiple matching locations
* Validate user location selection
* Display:

  * Temperature
  * Feels Like
  * Humidity
  * Wind Speed
  * Weather Description
* Retrieve weather forecasts
* Generate daily forecast summaries
* JSON output with `--json`
* Handle API failures
* Provide user-friendly error messages

---

## Tech Stack

* **Language:** Python 3
* **CLI:** `argparse`
* **HTTP:** `requests`
* **Testing:** `pytest`, `unittest.mock`
* **Configuration:** `python-dotenv`
* **APIs:** OpenWeather Geocoding, Current Weather, and Forecast APIs
* **CI:** GitHub Actions
* **Dependency Management:** Dependabot
* **Version Control:** Git and GitHub

---

## Project Structure

```text
weather-cli/
│
├── main.py              # Controls the application flow
├── cli.py               # Handles command-line arguments
├── geocode.py           # Gets latitude and longitude
├── weather.py           # Fetches current weather data
├── forecast.py          # Fetches and processes forecast data
├── display.py           # Handles formatting and user interaction
├── config.py            # Stores configuration and API constants
│
├── tests/
│   ├── test_cli.py      # CLI tests
│   ├── test_display.py  # Display and location-selection tests
│   ├── test_geocode.py  # Geocoding tests
│   ├── test_weather.py  # Current weather tests
│   └── test_forecast.py # Forecast tests
│
├── docs/
│   ├── requirements.md
│   ├── HLD.md
│   └── LLD.md
│
├── .github/
│   ├── workflows/
│   │   └── python.yml   # GitHub Actions CI workflow
│   └── dependabot.yml   # Dependabot configuration
│
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example
```

---

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:pratik0157-hub/weather-cli.git
cd weather-cli
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**Linux/macOS:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the API key

Create a `.env` file in the project root:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

An example configuration is provided in `.env.example`.

---

## Usage

### Current Weather

Search for a city using the `--city` or `-c` option:

```bash
python3 main.py --city Pune
```

Example output:

```text
City: Pune

Temperature : 28°C
Feels Like  : 30°C
Humidity    : 74%
Wind Speed  : 3.5 m/s
Weather     : Broken Clouds
```

### Multiple Locations

If the entered city name matches multiple locations, the application displays the available locations and allows the user to select the required location.

### JSON Output

Use the `--json` option to receive the weather data in JSON format:

```bash
python3 main.py --city Pune --json
```

Example:

```json
{
    "coord": {
        "lon": 73.8553,
        "lat": 18.5196
    },
    "weather": [
        {
            "description": "broken clouds"
        }
    ],
    "main": {
        "temp": 28,
        "feels_like": 30,
        "humidity": 74
    }
}
```

The JSON output uses the weather data already retrieved by the application and does not require an additional weather API request.

---

## Forecast

The application also retrieves forecast data using the OpenWeather Forecast API.

The API provides multiple forecast entries throughout the forecast period. The application processes these entries by grouping them by date and generates a daily summary containing:

* Maximum temperature
* Minimum temperature
* Most common weather description

This separates **data retrieval** from **data processing**, making the forecast functionality easier to test independently.

---

## Testing

The project uses **pytest** for automated testing.

Run the complete test suite from the project root:

```bash
python3 -m pytest
```

Tests currently cover:

* CLI argument parsing
* Required city argument
* JSON command-line option
* Location selection
* Invalid location input
* Geocoding functionality
* Current weather functionality
* Forecast API functionality
* Forecast summary processing
* API success cases
* API failure cases
* Empty forecast data

External API requests are mocked during tests using `unittest.mock`. This allows the tests to use controlled API responses without making real requests.

### Code Coverage

Test coverage is measured using **pytest-cov**:

```bash
python3 -m pytest --cov=. --cov-report=term-missing
```

Coverage reports are uploaded to **Codecov** through GitHub Actions.

[![codecov](https://codecov.io/gh/pratik0157-hub/weather-cli/graph/badge.svg)](https://codecov.io/gh/pratik0157-hub/weather-cli)

---

## Continuous Integration

GitHub Actions automatically runs the test suite on:

* Pushes to `main`
* Pull Requests targeting `main`

The CI workflow uses a matrix to test the application across:

* Ubuntu
* Windows
* macOS
* Multiple Python versions

Dependency caching is also used to avoid unnecessarily downloading unchanged dependencies on every CI run.

The CI workflow also generates and uploads test coverage reports to Codecov.

This helps catch compatibility issues, track test coverage, and prevent broken changes from being merged into `main`.


---

## Dependency Management

The project uses **Dependabot** to monitor dependencies and create Pull Requests when updates are available.

Dependabot updates go through the same Pull Request and CI workflow, allowing dependency changes to be tested before they are merged.

---

## Development Workflow

Development follows a feature-branch and Pull Request workflow:

```text
main
  ↓
feature branch
  ↓
make changes
  ↓
run tests
  ↓
commit
  ↓
push branch
  ↓
Pull Request
  ↓
GitHub Actions
  ↓
review
  ↓
merge into main
```

This workflow is used to practice development processes beyond simply writing and pushing code.

---


### Future Improvement Ideas

* [ ] Improve forecast test coverage
* [ ] Improve terminal output
* [ ] Unit conversion
* [ ] Releases and version tags
* [ ] Release artifacts
* [ ] Package the application as an installable CLI

---

## License

MIT License
