import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(API_URL, params={"key": API_KEY, "q": "Paris"})
    print("Performing request to Weather API for city Paris...")
    data_location = response.json()['location']
    data_weather = response.json()['current']
    print(f"{data_location['name']}/{data_location['country']} "
          f"{data_location['localtime']} "
          f"Weather: {data_weather['temp_c']} Celsius, {data_weather['condition']['text']}")


if __name__ == "__main__":
    get_weather()
