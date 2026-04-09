import os

import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
SECRET_KEY = os.environ.get("API_KEY")
WEATHER_URL = f"{BASE_URL}?q={CITY}&key={SECRET_KEY}"


def get_weather() -> None:
    r = requests.get(WEATHER_URL)
    print(r.json())


if __name__ == "__main__":
    get_weather()
