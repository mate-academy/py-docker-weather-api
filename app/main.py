import os
import requests


API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> dict:
    """Fetch current weather data for the specified city."""
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no"
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()


def main() -> None:
    """Display current temperature and condition for the city."""
    weather_data = get_weather()
    temp = weather_data["current"]["temp_c"]
    description = weather_data["current"]["condition"]["text"]
    print(f"Current weather in {CITY}: {temp}°C, {description}")


if __name__ == "__main__":
    main()