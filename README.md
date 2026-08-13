# Weather CLI

[![Python CI](https://github.com/pratik0157-hub/weather-cli/actions/workflows/python.yml/badge.svg)](https://github.com/pratik0157-hub/weather-cli/actions/workflows/python.yml)

A simple command-line weather application built in Python.

The user provides a city name, the program finds its latitude and longitude using the OpenWeather Geocoding API, then fetches the current weather using the OpenWeather Current Weather API.

> This project was built as part of my journey to learn Python and software engineering by building real applications instead of only solving coding problems.

This project is being developed to practice:

- Python modules
- `argparse`
- Working with REST APIs
- JSON
- Project organization
- Error handling
- Automated testing
- Git and GitHub workflows
- Continuous Integration
- Basic software engineering practices

---

## Features

- Search weather by city name
- City name is provided using the `--city` / `-c` command-line option
- City name is required
- City option can be placed anywhere in the command
- Automatically convert city name to latitude and longitude
- Handles multiple matching locations by allowing the user to select a location
- Displays:
  - Temperature
  - Feels Like
  - Humidity
  - Wind Speed
  - Weather Description
- JSON output using the `--json` option
- Handles invalid location selections
- Handles API failures
- Friendly error messages
- Command-line interface using `argparse`

---

## Technologies Used

- Python 3
- `argparse`
- `requests`
- `pytest`
- `python-dotenv`
- OpenWeather Geocoding API
- OpenWeather Current Weather API
- GitHub Actions

---

## Project Structure

```text
weather-cli/
│
├── main.py              # Controls the flow of the program
├── cli.py               # Handles command-line arguments
├── geocode.py           # Gets latitude & longitude
├── weather.py           # Fetches weather data
├── display.py           # Formats and displays weather data
├── config.py            # Stores configuration and API constants
│
├── tests/
│   ├── test_cli.py      # Tests CLI argument parsing
│   ├── test_display.py  # Tests location selection/display logic
│   ├── test_geocode.py  # Tests geocoding functionality
│   └── test_weather.py  # Tests weather API functionality
│
├── docs/
│   ├── requirements.md
│   ├── HLD.md
│   └── LLD.md
│
├── .github/
│   └── workflows/
│       └── python.yml   # GitHub Actions CI workflow
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

### 5. Create a `.env` file

Create a `.env` file in the project root:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

An example configuration is provided in `.env.example`.

---

## Usage

### Search for weather

The city must be provided using the `--city` or `-c` option.

```bash
python3 main.py --city Pune
```

The city option can also be used with other command-line options:

```bash
python3 main.py --city "New York"
```

### Example output

```text
City: Pune

Temperature : 28°C
Feels Like  : 30°C
Humidity    : 74%
Wind Speed  : 3.5 m/s
Weather     : Broken Clouds
```

### Multiple matching locations

If the entered city name matches multiple locations, the application displays the available locations and allows the user to select the required one.

### JSON output

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

The JSON output uses the data returned by the weather API and does not require an additional API request.

---

## Testing

This project uses **pytest** for automated testing.

Run the complete test suite from the project root:

```bash
python3 -m pytest
```

The test suite currently covers:

- CLI argument parsing
- Required city argument
- JSON command-line option
- Location selection
- Geocoding functionality
- Weather API functionality
- API failure cases
- Invalid location selection

The project also uses GitHub Actions to run the test suite automatically.

---

## Continuous Integration

GitHub Actions automatically runs the test suite for:

- Pushes to `main`
- Pull requests targeting `main`

The CI workflow uses a matrix to test the project across:

- Ubuntu
- Windows
- macOS

and currently tests multiple Python versions.

This helps catch compatibility problems and ensures that changes do not break existing functionality before they are merged into `main`.

---

## Git and GitHub Workflow

The project is also being used to practice a real-world Git workflow.

Development generally follows:

```text
main
  ↓
feature branch
  ↓
make changes
  ↓
commit
  ↓
push branch
  ↓
Pull Request
  ↓
GitHub Actions
  ↓
tests
  ↓
merge into main
```

Features are developed in separate branches and merged into `main` through pull requests.

---

## What I Learned

While building this project I learned:

- Making HTTP requests with `requests`
- Working with REST APIs
- Parsing JSON responses
- Using `argparse` for command-line interfaces
- Using required and optional command-line arguments
- Using boolean CLI flags with `action="store_true"`
- Handling multiple API results
- Handling invalid user input
- Handling API failures
- Writing automated tests with `pytest`
- Testing exceptions with `pytest.raises`
- Organizing a Python project into modules
- Using environment variables for API keys
- Creating and using virtual environments
- Writing GitHub Actions workflows
- Running tests across multiple operating systems
- Using Git branches and pull requests
- Using CI to validate changes before merging
- Improving code structure and readability

---

## Development Progress

The project is being developed incrementally, with each feature implemented, tested, documented, and merged separately.

### Completed

- [x] Basic weather CLI
- [x] City geocoding
- [x] Multiple location selection
- [x] Current weather information
- [x] API error handling
- [x] Automated tests with pytest
- [x] Required `--city` / `-c` argument
- [x] JSON output
- [x] GitHub Actions CI
- [x] Multi-platform CI testing
- [x] Feature branch and pull request workflow

### Planned

- [ ] Weather forecast
- [ ] Improve terminal output
- [ ] Unit conversion
- [ ] Improve project test coverage
- [ ] Dependabot
- [ ] Releases and version tags
- [ ] Release artifacts
- [ ] Package as an installable CLI
- [ ] Further project/documentation polish

---

## Future Improvements

Some planned improvements include:

- Colored terminal output
- Weather icons
- Unit conversion
- Weather forecast
- Save recent searches
- Improve test coverage
- Dependabot dependency updates
- GitHub releases and versioning
- Package the application as an installable CLI

---

## License

MIT License