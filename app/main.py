import os

import requests
from dotenv import load_dotenv

#  docker pull softheart/weather-api
load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")

    result = requests.get(URL, params={"key": API_KEY, "q": FILTERING})

    if result.status_code == 200:
        result = result.json()
        location = result["location"]
        weather = result["current"]
        data = (
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {weather['temp_c']} Celsius, "
            f"{weather['condition']['text']}"
        )
        print(data)


if __name__ == "__main__":
    get_weather()
