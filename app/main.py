import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY environment variable not set")

BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    try:
        response = requests.get(f"{BASE_URL}?key={API_KEY}&q={CITY}")
        response.raise_for_status()

        data = response.json()

        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Performing requests to Weather API for city {CITY}...")
        print(f"{CITY}/{country} {localtime} - {temperature}°C, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


if __name__ == "__main__":
    get_weather()
