import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
WEATHER_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    print("WORLD CITIES WEATHER")
    location = input("Enter town:")
    payload = {"key": API_KEY, "q": location}
    response = requests.get(WEATHER_URL, params=payload)
    if response.status_code == 200:
        country = response.json()["location"]["country"]
        city = response.json()["location"]["name"]
        local_time = response.json()["location"]["localtime"]
        last_updated = response.json()["current"]["last_updated"]
        temperature = response.json()["current"]["temp_c"]
        condition = response.json()["current"]["condition"]["text"]
        wind_kph = response.json()["current"]["wind_kph"]
        wind_dir = response.json()["current"]["wind_dir"]
        pressure = response.json()["current"]["pressure_mb"]

        print(f"Location: {country} / {city}")
        print(f"local time: {local_time}")
        print(f"Weather: {temperature} C, {condition}")
        print(f"Wind speed: {wind_kph} kph")
        print(f"Direction of the wind: <{wind_dir}>")
        print(f"Pressure: {pressure} mb")
        print(f"Last updated: {last_updated}")
    else:
        print("Page not found. Possibly incorrect data. Try again")

if __name__ == "__main__":
    get_weather()
