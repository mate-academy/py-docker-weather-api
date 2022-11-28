import os

import requests

URL = "http://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    params = {
        "key": os.environ.get("API_KEY"),
        "q": CITY,
    }
    data = requests.get(url=URL, params=params).json()

    for key, value in data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    get_weather()
