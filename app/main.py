import os
import sys

import requests


API_KEY = os.environ.get("API_KEY")
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
    if response.status_code == 200:

        data = response.json()
        location = data.get("location")
        current = data.get("current")
        condition = current.get("condition")

        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} Celsius, {condition['text']}"
        )
        sys.exit(0)

    elif response.status_code == 401:
        print("Wrong API key")
        sys.exit(1)

    else:
        print("Can't access to Weather API")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
