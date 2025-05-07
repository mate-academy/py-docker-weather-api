"""Weather API service for getting current weather in Paris."""
import os
import sys
from typing import Dict, Any

import requests
from dotenv import load_dotenv

# Constants
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> Dict[str, Any]:
    """
    Get current weather for Paris from Weather API.

    Returns:
        Dict[str, Any]: Weather data
    """
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set")
        sys.exit(1)

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no"
    }

    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)


def main() -> None:
    """Print current weather information for Paris."""
    load_dotenv()  # Load environment variables first
    weather_data = get_weather()

    current = weather_data["current"]
    location = weather_data["location"]

    print(f"Current weather in {location['name']}:")
    print(f"Temperature: {current['temp_c']}°C")
    print(f"Condition: {current['condition']['text']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Wind: {current['wind_kph']} km/h")


if __name__ == "__main__":
    main()
