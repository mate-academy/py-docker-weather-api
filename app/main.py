import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY", "953f36955f3946dc856163937231212")
CITY = "Paris"

DISPLAY_FORMAT = (
    "{location[name]}/{location[country]} "
    "{current[last_updated]} "
    "Weather: {current[temp_c]} Celsius, "
    "{current[condition][text]}"
)


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }
    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(API_URL, params=params)
    data = response.json()
    print(DISPLAY_FORMAT.format(
        location=data["location"],
        current=data["current"]
    ))


if __name__ == "__main__":
    get_weather()
