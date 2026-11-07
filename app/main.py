import os

import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ["API_KEY"]
    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(
        BASE_URL,
        params={"key": api_key, "q": CITY},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()
    location = data["location"]
    current = data["current"]
    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} Weather: "
        f"{current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
