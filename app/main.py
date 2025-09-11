import os

import requests


API_KEY = os.environ["API_KEY"]
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> str:
    print("Performing request to Weather API for city Paris...")
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": CITY,
            "aqi": "no"
        }
    )
    data = response.json()
    location = data.get("location")
    current = data.get("current")
    condition = current.get("condition")

    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, {condition['text']}"
    )


if __name__ == "__main__":
    get_weather()
