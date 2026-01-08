import os
import sys
import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY_NAME = "Paris"
API_KEY_ENV_NAME = "WEATHER_API_KEY"


def get_weather() -> None:
    api_key = os.getenv(API_KEY_ENV_NAME)

    if not api_key:
        print("ERROR: WEATHER_API_KEY environment variable is not set.")
        sys.exit(1)

    params = {
        "key": api_key,
        "q": CITY_NAME,
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    weather_data = response.json()
    print(weather_data)


if __name__ == "__main__":
    get_weather()
