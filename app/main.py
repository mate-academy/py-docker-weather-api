import os
from datetime import datetime

import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    try:
        result = requests.get(URL, params={"key": API_KEY, "q": CITY})
        result.raise_for_status()
        data = result.json()["current"]
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        weather_content = (
            f"Performing request to Weather API for city {CITY}...\n"
            f"{CITY}/France {current_time}"
            f" Weather: {data['temp_c']} Celsius, "
            f"{data['condition']['text']}"
        )

        print(weather_content)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_weather()
