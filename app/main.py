import os
import sys

import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY_ENV = "API_KEY"


def get_weather() -> None:
    api_key = os.environ.get(API_KEY_ENV)
    if not api_key:
        sys.exit(f"Environment variable {API_KEY_ENV} is not set")

    print(f"Performing request to Weather API for city {CITY}...")
    weather_response = requests.get(URL, params={"key": api_key, "q": CITY})
    weather_response.raise_for_status()
    weather = weather_response.json()

    city_name = weather["location"]["name"]
    country = weather["location"]["country"]
    local_time = weather["location"]["localtime"]
    temperature = weather["current"]["temp_c"]
    condition = weather["current"]["condition"]["text"]

    print(
        f"{city_name}/{country} {local_time} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
