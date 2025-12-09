import os

import requests

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"

URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
    }
    response = requests.get(URL, params=params)
    print(response.json())


if __name__ == "__main__":
    get_weather()
