import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY is not set")
        return

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no",
    }

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        print("Failed to get weather data.")
        return

    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location}/{country} {localtime} "
          f"Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
