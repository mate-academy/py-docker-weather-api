import os

import requests

API_KEY = os.environ["API_KEY"]
CITY = "Paris"
WEATHER_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(WEATHER_URL, params={"key": API_KEY, "q": CITY})
    response.raise_for_status()
    data = response.json()

    location = data["location"]
    current = data["current"]
    city_name = location["name"]
    country = location["country"]
    local_time = location["localtime"]
    temp_c = current["temp_c"]
    condition = current["condition"]["text"]

    print(
        f"{city_name}/{country} {local_time} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
