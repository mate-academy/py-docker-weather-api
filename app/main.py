import os

from dotenv import load_dotenv

import requests


load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    weather_url = "http://api.weatherapi.com/v1"
    current_weather = "/current.json"
    url = f"{weather_url}{current_weather}?key={API_KEY}&q={CITY}"
    response = requests.get(url).json()
    print(response)
    print(response["location"]["name"])
    print(response["location"]["country"])
    print("temperature in celsius", response["current"]["temp_c"])


if __name__ == "__main__":
    get_weather()
