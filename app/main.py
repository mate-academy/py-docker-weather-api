import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"

LOCATION = "Paris"

API_KEY = os.getenv("WEATHER_API_KEY")

if not API_KEY:
    raise Exception("Weather API key not found.")


def get_weather() -> None:
    response = requests.get(URL + f"?key={API_KEY}" + f"&q={LOCATION}")
    data = response.json()

    country = data["location"]["country"]
    last_update = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    text = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {LOCATION}...")
    print(
        f"{LOCATION}/{country} {last_update} "
        f"Weather: {temperature} Celsius, {text}"
    )


if __name__ == "__main__":
    get_weather()
