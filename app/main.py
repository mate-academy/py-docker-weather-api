import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
PARAMS = {"key": API_KEY, "q": "Paris"}


def get_weather() -> None:
    res = requests.get(URL, params=PARAMS).json()

    city = res["location"]["name"]
    country = res["location"]["country"]
    date = res["location"]["localtime"]
    temperature = res["current"]["temp_c"]
    condition = res["current"]["condition"]["text"]

    print("Performing request to Weather API for city Paris...")
    print(f"{city}/{country} {date} "
          f"Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
