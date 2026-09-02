import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("WEATHER_API_KEY")
    response = requests.get(f"{URL}?key={api_key}&q={CITY}")

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Помилка: {response.status_code}")

if __name__ == "__main__":
    get_weather()
