from __future__ import annotations

import os
import sys
from datetime import datetime

import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    """Fetch and print current weather for Paris."""
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        sys.exit(1)

    print(
        f"Performing request to Weather API for city {CITY}..."
    )

    params = {"key": api_key, "q": CITY}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    city_name = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print(
        f"{city_name}/{country} {now} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
