import os

import requests


API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params={
            "key": API_KEY,
            "q": "Paris"
        },
    )
    data = response.json()
    time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print("Performing request to Weather API for city Paris...")
    print(f"Paris/France {time} Weather: {temperature}, {condition}")


if __name__ == "__main__":
    get_weather()
