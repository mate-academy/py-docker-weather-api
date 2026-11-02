import os
import sys

import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY_ENV = "API_KEY"


def get_weather() -> None:
    api_key = os.environ.get(API_KEY_ENV)
    if not api_key:
        sys.exit(f"Environment variable {API_KEY_ENV} is not set")

    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(URL, params={"key": api_key, "q": CITY})
    response.raise_for_status()
    data = response.json()

    location = data["location"]
    current = data["current"]

    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
    