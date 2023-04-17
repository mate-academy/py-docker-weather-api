import os
from pprint import pprint

import requests


API_KEY = os.getenv("API_KEY")

FILTER_BY_CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTER_BY_CITY}

    response = requests.get(URL, params=params)

    pprint(response.content)


if __name__ == "__main__":
    get_weather()
