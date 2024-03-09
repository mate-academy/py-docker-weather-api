import os

import requests


CURRENT_WEATHER_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(key: str) -> None:
    req = requests.get(
        CURRENT_WEATHER_URL,
        params={
            "key": key,
            "q": "Paris"
        }
    )

    print(req.text)


if __name__ == "__main__":
    API_KEY = os.environ.get("API_KEY")
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set")
    get_weather(API_KEY)
