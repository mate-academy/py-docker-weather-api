import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL_WEATHER = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")

    payload = {"q": CITY, "key": API_KEY}
    response = requests.get(URL_WEATHER, params=payload)
    response_data = response.json()

    country = response_data["location"]["country"]
    localtime = response_data["location"]["localtime"]
    temperature = response_data["current"]["temp_c"]
    condition = response_data["current"]["condition"]["text"]

    print(
        f"{CITY}/{country} {localtime} Weather: "
        f"{temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
