import os

import requests

API_KEY = os.environ.get("API_KEY")

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    """
    Sends a request to the WEATHER_API_URL and print the current
    weather information for the city specified by the CITY constant.
    """
    print(f"Performing request to Weather API for city {CITY}...")

    params = {"key": API_KEY, "q": CITY}
    response = requests.get(WEATHER_API_URL, params=params).json()

    country = response["location"]["country"]
    _datetime = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(
        f"{country}/{CITY} {_datetime} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
