import os

import requests


LOCATION = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"

    params = {"key": API_KEY, "q": LOCATION}

    response = requests.get(url, params=params)

    print(response.content)


if __name__ == "__main__":
    get_weather()
