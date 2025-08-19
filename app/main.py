import json
import os
import sys

import environ
import requests

FILTERING = "Paris"
URL = "http://api.weatherapi.com/v1/forecast.json"


def get_weather() -> None:
    environ.Env.read_env()
    api_key = os.environ.get("API_KEY")
    print("Performing request to Weather API for city Paris")
    if not api_key:
        print("API key was not provided, exiting app")
        sys.exit()
    response = requests.get(
        f"{URL}?q={FILTERING}&key={api_key}",
    )
    if response.status_code == 200:
        data = response.json()
        location = data["location"]
        current = data["current"]
        print(f"{location['name']}/{location['country']} "
              f"{location['localtime']} "
              f"Weather: {current['temp_c']} Celsius, "
              f"{current['condition']['text']}")
    else:
        print(response.content)


if __name__ == "__main__":
    get_weather()
