import os

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("SECRET_API_KEY")
CITY = "Paris"


def get_weather() -> None:
    weather_paris = requests.get(f"{BASE_URL}?key={API_KEY}&q={CITY}")

    data = weather_paris.json()

    if weather_paris.status_code == 200:
        temperature = data["current"]["temp_c"]
        wind = data["current"]["wind_mph"]
        humidity = data["current"]["humidity"]
        pressure = data["current"]["pressure_mb"]

        print(
            f"In this day, weather in city {CITY}:\n"
            f"Temperature: {temperature}°C\n"
            f"Wind: {wind} km/h\n"
            f"Humidity: {humidity} %\n"
            f"Pressure: {pressure} P\n"
            f"And let problems and "
            f"disagreements not make "
            f"the weather in your life, "
            f"may you be lucky and be healthy:)"
        )
    else:
        print("You have bad API_KEY")


if __name__ == "__main__":
    get_weather()
