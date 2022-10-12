import json
import os

import requests


WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather():
    print("Performing request to Weather API for city Paris...")
    api_key = os.environ.get("API_KEY", None)
    if api_key is not None:
        resp = requests.get(
            WEATHER_API_URL,
            params={
                "key": api_key,
                "q": "Paris",
                "aqi": "no"
            }
        )
        data = json.loads(resp.content)
        location = data["location"]
        current = data["current"]
        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} Celsius, "
            f"{current['condition']['text']}"
        )
        return
    print("You must pass environment variable API_KEY!")


if __name__ == "__main__":
    get_weather()
