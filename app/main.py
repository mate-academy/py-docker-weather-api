import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    params = {
        "key": api_key,
        "q": CITY,
    }

    response = requests.get(URL, params=params)

    data = response.json()

    print(data)


if __name__ == "__main__":
    get_weather()
