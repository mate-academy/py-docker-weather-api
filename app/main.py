import os
import sys

import requests


# Constants defined at module level
CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    # 1. Get API Key from Environment Variable
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable not set.")
        sys.exit(1)

    print(f"Performing request to Weather API for city {CITY}...")

    try:
        response = requests.get(f"{BASE_URL}?key={api_key}&q={CITY}")
        response.raise_for_status()
        data = response.json()

        # Extract data using double quotes for keys
        location = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        # Broken into multiple lines to satisfy line-length limits
        print(
            f"{location}/{country} {local_time} "
            f"Weather: {temp_c} Celsius, {condition}"
        )

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
