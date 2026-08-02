import os

import requests


API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> dict:
    params = {
        "key": API_KEY,
        "q": CITY
    }
    return requests.get(url=URL, params=params).json()


if __name__ == "__main__":
    print(get_weather())
