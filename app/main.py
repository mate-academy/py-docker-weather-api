import requests
import os
import json


URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")
FILTERING = "Paris"


def get_weather() -> None:
    weather = requests.get(URL + f"key={API_KEY}&q={FILTERING}")

    print(f"Performing request to Weather API for city {FILTERING}...")

    data = json.loads(weather.text)

    print(
        data["location"]["name"],
        "/",
        data["location"]["country"],
        data["location"]["localtime"],
        "Weather: ",
        data["current"]["temp_c"],
        "Celsius, ",
        data["current"]["condition"]["text"],
    )


if __name__ == "__main__":
    get_weather()
