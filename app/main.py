import os

import requests

from dotenv import load_dotenv


def configure():
    load_dotenv()


def get_weather():
    configure()

    url = "https://api.weatherapi.com/v1/current.json"

    city = "Paris"

    params = {
        "key": os.getenv("API_KEY"),
        "q": city,
    }

    print(f"Performing request to Weather API for city {city}...")

    res = requests.get(url=url, params=params)

    data = res.json()

    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{city}/{country} {local_time} Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
