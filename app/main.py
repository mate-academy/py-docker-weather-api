import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
REQUEST_TIMEOUT = 10


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(
        URL,
        params={"key": os.environ["API_KEY"], "q": CITY},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    weather = response.json()

    location = weather["location"]
    current = weather["current"]
    city = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    temperature = current["temp_c"]
    condition = current["condition"]["text"]
    print(
        f"{city}/{country} {localtime} Weather: "
        f"{temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
