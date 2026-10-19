import os
import sys

import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        sys.exit("Error: API_KEY environment variable is not set.")

    response = requests.get(
        API_URL,
        params={"key": api_key, "q": CITY},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    name = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    condition = data["current"]["condition"]["text"]
    temp = data["current"]["temp_c"]
    feels_like = data["current"]["feelslike_c"]
    wind = data["current"]["wind_kph"]
    humidity = data["current"]["humidity"]

    print(f"Performing request to Weather API for city {name}...")
    print(f"Weather in {name}, {country}")
    print(f"Local time: {localtime}")
    print(f"Condition: {condition}")
    print(f"Temperature: {temp} °C")
    print(f"Feels like: {feels_like} °C")
    print(f"Wind: {wind} kph")
    print(f"Humidity: {humidity}%")


if __name__ == "__main__":
    get_weather()
