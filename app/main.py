import os

import requests

API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY, "q": "Paris"})
    data = response.json()

    location = data["location"]["country"]
    time = data["location"]["time"]
    temperature = str(data["current"]["temperature"]) + " Celsius"
    condition = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city Paris...")
    print(f"{location} {time} Weather: {temperature}, {condition}")


if __name__ == "__main__":
    get_weather()
