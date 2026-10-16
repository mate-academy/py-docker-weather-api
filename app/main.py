import os
import sys

import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
LANGUAGE = "uk"
API_KEY_ENV = "API_KEY"
TIMEOUT = 10


def get_weather(city: str) -> None:
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        sys.exit(f"Error: environment variable {API_KEY_ENV} is not set")

    params = {"key": api_key, "q": city, "lang": LANGUAGE}

    response = requests.get(URL, params=params, timeout=TIMEOUT)

    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    get_weather(CITY)
