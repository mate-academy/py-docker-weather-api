import os

import requests


API_KEY = os.environ.get("API_KEY")
API_URL = "https://api.weatherapi.com/v1/current.json?"
CITY_NAME = "Paris"


def get_weather() -> None:
    url = (API_URL + "key=" + API_KEY + "&q=" + CITY_NAME)

    res = requests.get(url)
    print(res.json())


if __name__ == "__main__":
    get_weather()
