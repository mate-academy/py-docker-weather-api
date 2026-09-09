import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL_WEATHER = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")

    payload = {"q": "Paris", "key": API_KEY}
    response = requests.get(URL_WEATHER, params=payload)
    response_data = response.json()

    localtime = response_data["location"]["localtime"]
    temperature = response_data["current"]["temp_c"]
    condition = response_data["current"]["condition"]["text"]

    print(
        f"Paris/France {localtime} Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
