import os

import requests

SECRET_KEY = os.environ.get("API_KEY")
CITY = "Paris"
WEATHER_URL = f"https://api.weatherapi.com/v1/current.json?q={CITY}&key={SECRET_KEY}"


def get_weather() -> None:
    r = requests.get(WEATHER_URL)
    print(r.json())


if __name__ == "__main__":
    get_weather()
