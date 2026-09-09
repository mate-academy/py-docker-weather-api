import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city_name = "Paris"
    res = requests.get(API_URL, params={"key": api_key, "q": city_name})
    data = res.json()

    print(f"{data["location"]["name"]}/{data["location"]["country"]}"
          f" {data["location"]["localtime"]}"
          f" Weather: {data["current"]["temp_c"]} Celsius, "
          f" {data["current"]["condition"]["text"]}")


if __name__ == "__main__":
    get_weather()
