import os

import requests


API_KEY = os.getenv("API_KEY")
CITY = "Odesa"


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"

    params = {"key": API_KEY, "q": CITY}

    response = requests.get(url, params=params).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    date = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...")
    print(
        f"{city}/{country} {date} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
