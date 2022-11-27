import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:

    response = requests.get(
        url=URL,
        params={
            "key": API_KEY,
            "q": CITY,
        }
    ).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    date = response["location"]["localtime"]
    temp = response["current"]["temp_c"]
    description = response["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {CITY}...")
    print(f"{city}/{country} {date} Weather: {temp} Celsius, {description}")


if __name__ == "__main__":
    get_weather()
