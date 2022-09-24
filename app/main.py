import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
KEY = os.getenv("API_KEY")


def get_weather():

    params = {
        "key": KEY,
        "q": "Paris"
    }

    res = requests.get(URL, params=params).json()
    city = res["location"]["name"]
    country = res["location"]["country"]
    localtime = res["location"]["localtime"]
    temp = res["current"]["temp_c"]
    condition = res["current"]["condition"]["text"]

    print("Performing request to Weather API for city Paris...")
    print(f"{city}/{country} {localtime} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
