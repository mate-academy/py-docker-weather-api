import os

import requests

API_URL = "https://api.weatherapi.com/v1/current.json"

CITY_NAME = "Paris"


def get_weather() -> None:

    try:
        api_key = os.environ["API_KEY"]
        if not api_key:
            print("Error: API_KEY environment variable is not set.")
            exit(1)
        url = (f"{API_URL}?key={api_key}&q={CITY_NAME}&aqi=no")
        response = requests.get(url).json()
        location_info = response["location"]
        current_info = response["current"]
        print("Performing request to Weather API for city Paris...")
        print(
            f"Paris/France {location_info['localtime']} "
            f"Weather: {current_info['temp_c']} Celsius, "
            f"{current_info['condition']['text']}"
        )
    except KeyError:
        print("Check your API_KEY")


if __name__ == "__main__":
    get_weather()
