import os
from datetime import datetime

import requests

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    result = requests.get(URL)
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


if __name__ == "__main__":
    get_weather()
