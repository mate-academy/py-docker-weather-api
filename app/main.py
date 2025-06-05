import os
import requests
import sys

API_BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY_TO_QUERY = "Paris"


def get_weather(api_key: str, city: str) -> dict | None:
    """Fetches current weather data for a given city."""
    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }
    try:
        response = requests.get(API_BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}", file=sys.stderr)
        return None
    except ValueError:
        print("Error: Could not decode JSON response from API.",
              file=sys.stderr)
        return None


def display_weather(weather_data: dict) -> None:
    """Prints weather information in a readable format."""
    if not weather_data:
        return
    try:
        location = weather_data["location"]
        current = weather_data["current"]

        print(f"Current weather in {location['name']}, "  # noqa: Q000, E231
              f"{location['country']}:")  # noqa: Q000, E231
        print(f"  Temperature: {current['temp_c']}°C "  # noqa: Q000
              f"({current['temp_f']}°F)")  # noqa: Q000
        print(f"  Condition: {current['condition']['text']}")  # noqa: Q000
        print(f"  Wind: {current['wind_kph']} kph, "  # noqa: Q000, E501
              f"direction {current['wind_dir']}")  # noqa: Q000, E501
        print(f"  Humidity: {current['humidity']}%")  # noqa: Q000
        print(f"  Last updated: {current['last_updated']}")  # noqa: Q000
    except KeyError as e:
        print(f"Error: Unexpected data structure from API - missing key {e}",
              file=sys.stderr)


if __name__ == "__main__":
    api_key_from_env = os.environ.get("API_KEY")

    if not api_key_from_env:
        print("Error: API_KEY environment variable not set.", file=sys.stderr)
        print("Please set it using -e API_KEY=<your_key> for the Docker container.",  # noqa: E501
              file=sys.stderr)
        sys.exit(1)

    weather_info = get_weather(api_key_from_env, CITY_TO_QUERY)

    if weather_info:
        display_weather(weather_info)
    else:
        print(f"Could not retrieve weather for {CITY_TO_QUERY}.",
              file=sys.stderr)
        sys.exit(1)
