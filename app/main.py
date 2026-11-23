import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("API_KEY environment variable is not set")
        return

    print(f"Performing request to Weather API for city {FILTERING}...")

    response = requests.get(
        URL, params={"key": api_key, "q": FILTERING}, timeout=10
    )
    response.raise_for_status()
    data = response.json()

    location = data["location"]
    current = data["current"]

    print(
        f"{location['name']}/{location['country']} {location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
