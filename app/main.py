import os
import sys

import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        sys.exit("Error: API_KEY environment variable is not set.")

    response = requests.get(
        API_URL,
        params={"key": api_key, "q": CITY},
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    location = data["location"]
    current = data["current"]

    print(f"Performing request to Weather API for city {location["name"]}...")
    print(f"Weather in {location["name"]}, {location["country"]}")
    print(f"Local time: {location["localtime"]}")
    print(f"Condition: {current["condition"]["text"]}")
    print(f"Temperature: {current["temp_c"]} °C")
    print(f"Feels like: {current["feelslike_c"]} °C")
    print(f"Wind: {current["wind_kph"]} kph")
    print(f"Humidity: {current["humidity"]}%")


if __name__ == "__main__":
    get_weather()
