import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")

URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(URL + f"key={API_KEY}" + "&" + f"q={CITY}")
    weather_data = response.json()
    location = weather_data["location"]
    current = weather_data["current"]
    message = f"{location['name']}/{location['country']} " \
              f"{location['localtime']} " \
              f"Weather: {current['temp_c']}, " \
              f"{current['condition']['text']}"
    print(f"Performing request to Weather API for city {CITY}")
    print(message)


if __name__ == "__main__":
    get_weather()
