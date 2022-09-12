import os
import time

import requests


def get_weather():
    url = "http://api.weatherapi.com/v1/current.json"
    key = os.getenv("API_KEY")
    params = {
        "key": key,
        "q": "Paris"
    }
    res = requests.get(url, params=params).json()
    city, country = res["location"]["name"], res["location"]["country"]
    localtime = res["location"]["localtime"]
    weather = res["current"]["temp_c"]
    condition = res["current"]["condition"]["text"]

    print("Performing request to Weather API for city Paris...")
    time.sleep(2)
    print(f"{city}/{country} {localtime} Weather: {weather} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
