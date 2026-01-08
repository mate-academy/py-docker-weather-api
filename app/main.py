import os
import sys

import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
AQI = "no"


def get_weather() -> None:
    api_key = os.getenv("api_key")

    if not api_key:
        print("Error: api_key environment variable is not set.")
        sys.exit(1)

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": AQI
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        data = response.json()

        current_temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        location = data["location"]["name"]

        print(f"Current weather in {location}:")
        print(f"Temperature: {current_temp}°C")
        print(f"Condition: {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
