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
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set")
    get_weather(api_key)
