import os

import requests

API = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(URL, params={"key": API, "q": CITY})
    data = response.json()

    location = CITY + "/" + data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = str(data["current"]["temp_c"]) + " Celsius"
    condition = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(f"{location} {localtime} Weather: {temp_c}, {condition}")


if __name__ == "__main__":
    get_weather()
