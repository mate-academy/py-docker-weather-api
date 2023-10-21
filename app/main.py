import os

import requests


API_KEY = os.environ.get("API_KEY", "1e1a09c423c045fd812121336231710 ")

BASE_URL = "https://api.weatherapi.com/v1/current.json"

CITY = "Paris"


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = requests.get(url=BASE_URL, params={"q": CITY, "key": API_KEY})
    json_data = response.json()
    city = json_data["location"]["name"]
    country = json_data["location"]["country"]
    localtime = json_data["location"]["localtime"]
    temp_c = json_data["current"]["temp_c"]
    condition = json_data["current"]["condition"]["text"]

    print(
        f"{city}/{country} {localtime} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
