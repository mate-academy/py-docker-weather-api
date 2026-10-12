import os

import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ["API_KEY"]
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(f"{BASE_URL}?key={API_KEY}&q={CITY}")
    print(response.json())


if __name__ == "__main__":
    get_weather()
