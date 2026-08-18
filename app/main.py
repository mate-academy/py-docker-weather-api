import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": CITY,
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    print(response.json())


if __name__ == "__main__":
    get_weather()
