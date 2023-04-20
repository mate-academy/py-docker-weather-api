import json
import os

import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "https://api.weather.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}

    response = requests.get(URL, params=params)

    weather_data = json.loads(response.content)
    location = weather_data["location"]
    weather = weather_data["weather"]

    print(
        f"{location['name']} | {location['country']}"
        f"Today's weather {weather['temp_c']} C,"
        f"{weather['condition']['text']}"
        f"Time: {location['localtime']}"
    )


if __name__ == "__main__":
    get_weather()
