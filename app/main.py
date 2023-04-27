import os
import requests

API_KEY = os.environ.get("API_KEY")
LOCATION = "Paris"
URL = "http://api.weatherapi.com/v1/current.json?"


def get_weather() -> None:

    print(f"Performing request to Weather API for city {LOCATION}...")
    params = {"key": API_KEY, "q": LOCATION}
    response = requests.get(URL, params=params).json()

    country = response["location"]["country"]
    _datetime = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(
        f"{country}/{LOCATION} {_datetime} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
