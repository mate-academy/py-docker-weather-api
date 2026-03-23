import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
DEFAULT_CITY = "Paris"


def get_weather(city: str = DEFAULT_CITY) -> None:
    if not API_KEY:
        raise ValueError("API_KEY must be set")

    params = {"key": API_KEY, "q": city}

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    condition = data["current"]["condition"]["text"]
    wind_kph = data["current"]["wind_kph"]

    print(f"Weather in {city}, {country}: ")
    print(f"Temperature: {temp_c}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")
    print(f"Wind speed: {wind_kph} kph")


if __name__ == "__main__":
    get_weather()
