import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"Current Weather in {CITY}:")
        print(f"Weather: {weather_data['current']['condition']['text']}")
        print(f"Temperature: {weather_data['current']['temp_c']} Celsius")
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    get_weather()
