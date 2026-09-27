import os

import requests

WEATHER_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ["API_KEY"]
    request_params = {
        "key": api_key,
        "q": CITY,
    }

    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(
        WEATHER_URL,
        params=request_params,
        timeout=10,
    )
    response.raise_for_status()

    weather_data = response.json()

    location_data = weather_data["location"]
    current_data = weather_data["current"]

    city = location_data["name"]
    country = location_data["country"]
    localtime = location_data["localtime"]
    temperature = current_data["temp_c"]
    condition = current_data["condition"]["text"]

    print(f"{city}/{country} {localtime} "
          f"Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
