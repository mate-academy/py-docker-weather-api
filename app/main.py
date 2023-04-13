import os

import requests


API_KEY = os.getenv("API_KEY")

FILTER = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTER}

    response = requests.get(URL, params=params)

    print(response.content)


if __name__ == "__main__":
    get_weather()
