import os

import requests


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params={
            "key": API_KEY,
            "q": "Paris"
        },
    )
    data = response.json()
    TIME = data["location"]["localtime"]
    TEMPERATURE = data["current"]["temp_c"]
    CONDITION = data["current"]["condition"]["text"]
    print("Performing request to Weather API for city Paris...")
    print(f"Paris/France {TIME} Weather: {TEMPERATURE}, {CONDITION}")


if __name__ == "__main__":
    get_weather()
