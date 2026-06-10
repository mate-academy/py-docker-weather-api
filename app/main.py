import os

import requests


BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        raise ValueError("API_KEY environment variable is required")

    response = requests.get(
        BASE_URL,
        params={"key": api_key, "q": CITY},
        timeout=10,
    )
    response.raise_for_status()

    weather_data = response.json()
    location = weather_data["location"]
    current = weather_data["current"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
