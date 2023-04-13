import os
import http

import requests

import exceptions
from dotenv import load_dotenv

load_dotenv("./.env")
KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"
WEATHER_ENDPOINT = "/current.json"
CITY = os.getenv("CITY", "Paris")
CITY_WEATHER_ENDPOINT = f"{BASE_URL}{WEATHER_ENDPOINT}?key={KEY}&q={CITY}"


def get_weather() -> None:
    """Get the weather for Paris"""
    res = requests.get(CITY_WEATHER_ENDPOINT)

    if res.status_code != http.HTTPStatus.OK:
        raise exceptions.BadWeatherApiRequestError()

    weather_data = res.json()

    weather_city = weather_data["location"]["name"]
    weather_country = weather_data["location"]["country"]
    weather_time = weather_data["location"]["localtime"]
    current_weather = f"Weather: {weather_data['current']['temp_c']} Celsius"
    weather_mood = weather_data["current"]["condition"]["text"]

    print(
        f"{weather_city}/{weather_country} "
        f"{weather_time} {current_weather}, "
        f"{weather_mood}"
    )


if __name__ == "__main__":
    get_weather()
