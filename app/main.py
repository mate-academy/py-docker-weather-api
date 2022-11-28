import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL + f"?key={API_KEY}&q={FILTERING}&aqi=no"
    ).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    localtime = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...")

    print(
        f"{city}/{country} {localtime} Weather: {temperature} "
        f"Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
