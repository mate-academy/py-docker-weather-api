from dotenv import load_dotenv
import os

import requests

load_dotenv()


def get_weather() -> None:
    API_KEY = os.environ["API_KEY"]
    URL = "https://api.weatherapi.com/v1/current.json?"
    CITY = "Paris"

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(f"{URL}key={API_KEY}&q={CITY}")
    result = response.json()
    location = result["location"]
    current = result["current"]

    print(f"{location['name']}/{location['country']} {location['localtime']}\n"
          f"Weather: {current['temp_c']} Celsius, "
          f"{current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
