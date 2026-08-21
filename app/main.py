import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(
        API_URL,
        params={"key": os.environ["API_KEY"], "q": CITY},
        timeout=10,
    )
    response.raise_for_status()
    weather_data = response.json()

    location = weather_data["location"]
    current_weather = weather_data["current"]
    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} Weather: "
        f"{current_weather['temp_c']} Celsius, "
        f"{current_weather['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
