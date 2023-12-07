import requests

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ["API_KEY"]


def get_weather() -> None:
    params = {
        "q": FILTERING,
        "key": API_KEY
    }

    response = requests.get(URL, params=params)

    print("Performing request to Weather API for city Paris...")

    if response.status_code != 200:
        print(f"Request error, Status code: {response.status_code} != 200")
        return

    weather_data = response.json()
    capital = weather_data["location"]["name"]
    country = weather_data["location"]["country"]
    localtime = weather_data["location"]["localtime"]
    temperature = weather_data["current"]["temp_c"]
    weather = weather_data["current"]["condition"]["text"]
    print(
        f"{capital}/{country} {localtime} "
        f"Weather: {temperature} Celsius, {weather}"
    )


if __name__ == "__main__":
    get_weather()
