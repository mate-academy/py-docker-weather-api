import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY_NAME = "Paris"


def get_weather() -> None:

    res = requests.get(API_URL, params={"key": API_KEY, "q": CITY_NAME})
    data = res.json()

    print(f"{data['location']['name']}/{data['location']['country']}"
          f" {data['location']['localtime']}"
          f" Weather: {data['current']['temp_c']} Celsius, "
          f" {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
