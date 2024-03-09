import os

import requests


CURRENT_WEATHER_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(key: str) -> None:
    request = requests.get(
        CURRENT_WEATHER_URL,
        params={
            "key": key,
            "q": "Paris"
        }
    )
    if request.status_code == 200:
        print(request.text)
    else:
        raise ValueError(f"Something went wrong. Status code is "
                         f"{request.status_code}, but expected 200")


if __name__ == "__main__":
    API_KEY = os.environ.get("API_KEY")
    if not API_KEY:
        raise ValueError("API_KEY environment variable not set")
    get_weather(API_KEY)
