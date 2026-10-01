import os

import requests


API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"

COMMAND = "docker pull illyaivanov/weather"


def get_weather() -> dict:
    params = {
        "key": API_KEY,
        "q": CITY,
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    weather = get_weather()
    print(weather)
