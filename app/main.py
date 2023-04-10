import os

import requests


def get_weather() -> None:
    CITY = "Paris"
    API_KEY = os.environ["API_KEY"]
    URL = "https://api.weatherapi.com/v1/current.json"
    response = requests.get(
        f"{URL}?key={API_KEY}&q={CITY}&aqi=no")
    data = response.json()
    location = data["location"]
    current = data["current"]
    print(f"Performing request to Weather API for city {CITY}...")
    print(
        (
            f"{location['country']}/"
            f"{location['name']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} "
            f"Celsius, {current['condition']['text']}"
        )
    )


if __name__ == "__main__":
    get_weather()
