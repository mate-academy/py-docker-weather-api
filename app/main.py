import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(API_URL, params={"key": API_KEY, "q": "Paris"})
    print("Performing request to Weather API for city Paris...")
    data_location = response.json()["location"]
    data_weather = response.json()["current"]
    print(f"{data_location['name']}/{data_location['country']} "  # noqa: Q000
          f"{data_location['localtime']} "  # noqa: Q000
          f"Weather: {data_weather['temp_c']} "  # noqa: Q000
          f"Celsius, {data_weather['condition']['text']}")  # noqa: Q000


if __name__ == "__main__":
    get_weather()
