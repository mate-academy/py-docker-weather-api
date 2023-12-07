import os
from http.client import HTTPResponse
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

WEATHER_BY_CITY_URL = "https://api.weatherapi.com/v1/current.json"
FILTERING_CITY = "France,Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    params = {
        "q": FILTERING_CITY,
        "key": API_KEY
    }

    response = requests.get(WEATHER_BY_CITY_URL, params=params)

    if not response.status_code == 200:
        print(f"Error getting weather. Please try again.")
        return None

    location_data = response.json()["location"]
    weather_data = response.json()["current"]
    print(
        f"Country: {location_data['country']}\n"
        f"City: {location_data['name']}\n"
        f"Time: {location_data['localtime']}\n"
        f"Temperature: {weather_data['temp_c']} ℃\n"
        f"Feels like: {weather_data['feelslike_c']} ℃\n"
        f"Condition: {weather_data['condition']['text']}\n"
        f"Wind: {weather_data['wind_kph']} km/h\n"
    )


if __name__ == "__main__":
    get_weather()
