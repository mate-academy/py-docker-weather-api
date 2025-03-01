import os
import requests
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        print("Error: API_KEY is not set")
        return

    CITY = "Paris"
    COUNTRY = "France"
    BASE_URL = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": "no"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        weather_desc = data["current"]["condition"]["text"]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

        print(f"{CITY}/{COUNTRY} {current_time} Weather: {temp} Celsius, {weather_desc}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
