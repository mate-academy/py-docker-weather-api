import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    payload = {
        "q": CITY,
        "key": API_KEY
    }
    response = requests.get(URL, params=payload)

    data = response.json()

    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(
        f"{CITY}/{country} {localtime} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
