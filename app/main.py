import os

import requests
from dotenv import load_dotenv

load_dotenv()
URL = "https://api.weatherapi.com/v1/current.json"
KEY = os.getenv("KEY")
FILTERING = "Paris"


def get_weather() -> None:
    payload = {
        "key": KEY,
        "q": FILTERING
    }
    request = requests.get(
        URL, payload
    )
    if request.status_code == 200:
        print_weather(request.json())
    else:
        print(f"Something wrong, status_code: {request.status_code}")


def print_weather(weather: dict) -> None:
    location = weather["location"]
    weather_current = weather["current"]

    print("Location")
    print(f"Country: {location["country"]}, City: {location["name"]}")
    print(f"TimeZone: {location["tz_id"]}, Time: {location["localtime"]}")
    print("-" * 50)
    print("Weather")
    print(f"Temperature: {weather_current["temp_c"]}")
    print(f"Day: {bool(weather_current["is_day"])}")
    print(f"Wind speed: {weather_current["wind_kph"]}km/h")


if __name__ == "__main__":
    get_weather()
