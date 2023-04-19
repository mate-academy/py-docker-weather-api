import os

import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    url = "https://api.weather.com/v1/current.json"

    params = {"key": API_KEY, "q": CITY}

    response = requests.get(url, params=params)

    print(response.content)


if __name__ == "__main__":
    get_weather()
