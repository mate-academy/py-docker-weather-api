import os

import requests
import json


API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    payload = {"q": CITY, "key": API_KEY}
    response = requests.get(URL, params=payload)
    info = json.loads(response.content)
    location_info = info["location"]
    weather_info = info["current"]

    print(
        f"{location_info['name']}/{location_info['country']} "
        f"{location_info['localtime']} "
        f"Weather: {weather_info['temp_c']} Celsius, "
        f"{weather_info['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
