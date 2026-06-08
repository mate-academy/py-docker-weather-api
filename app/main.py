import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(URL, params={"key": api_key, "q": CITY})
    data = response.json()

    city_name = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        f"{city_name}/{country} {localtime} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
