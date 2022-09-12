import os
import time

import requests


def get_weather():
    URL = "http://api.weatherapi.com/v1/current.json"
    KEY = os.getenv("API_KEY")
    params = {
        "key": KEY,
        "q": "Paris"
    }
    res = requests.get(URL, params=params).json()
    city, country = res["location"]["name"], res["location"]["country"]
    localtime = res["location"]["localtime"]
    weather = res["current"]["temp_c"]
    condition = res["current"]["condition"]["text"]

    print("Performing request to Weather API for city Paris...")
    time.sleep(2)
    print(f"{city}/{country} {localtime} Weather: {weather} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
