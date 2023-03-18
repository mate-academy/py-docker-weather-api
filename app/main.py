import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.environ.get("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json?"


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY, "q": "Paris"})
    weather_data = response.json()
    location = weather_data["location"]
    current = weather_data["current"]
    message = (f"{location['name']}/{location['country']}"
               f"{location['localtime']}"
               f"Weather: {current['temp_c']},"
               f"{current['condition']['text']}")
    print(f"Performing request to weather API for city Paris")
    print(message)


if __name__ == "__main__":
    get_weather()
