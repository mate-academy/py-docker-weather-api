import os

import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTERING}

    response = requests.get(URL, params=params)

    print(response.content)


if __name__ == "__main__":
    get_weather()
