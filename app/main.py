import os
import requests

from datetime import datetime

API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
FILTER = "Paris"


def get_weather() -> None:
    """Get current weather in Paris from weatherapi.com API"""
    params = {
        "key": API_KEY,
        "q": FILTER,
    }

    response = requests.get(URL, params=params)

    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    weather = response.json()

    print("Performing request to Weather API for city Paris...")
    print(f"Paris/France {datetime.now().strftime('%Y-%m-%d %H:%M')} "
          f"Weather: {weather['current']['temp_c']} Celsius, "
          f"{weather['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
