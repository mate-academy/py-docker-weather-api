import os

import requests
from typing import Dict

API_KEY = os.environ["API_KEY"]
FILTERING = "Paris"


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"

    params = {"key": API_KEY, "q": FILTERING}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data: Dict = response.json()
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Current weather in {FILTERING}: {temp_c}°C, {condition}")
    else:
        print("Failed to fetch weather data")


if __name__ == "__main__":
    get_weather()
