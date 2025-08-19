import json
import os
import sys

import environ
import requests


def get_weather() -> None:
    environ.Env.read_env()
    api_key = os.environ.get("API_KEY")
    print("Performing request to Weather API for city Paris")
    if not api_key:
        print("API key was not provided, exiting app")
        sys.exit()
    FILTERING = "Paris"
    URL = "http://api.weatherapi.com/v1/forecast.json"
    response = requests.get(
        f"{URL}?q={FILTERING}&key={api_key}",
    )
    data = json.loads(response.content)
    location = data["location"]
    current = data["current"]
    print(f"{location['name']}/{location['country']} {location['localtime']} "
          f"Weather: {current['temp_c']} Celsius, {current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
