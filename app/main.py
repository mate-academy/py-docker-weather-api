import os
import requests

WEATHER_API_KEY = os.getenv("API_KEY")

BASE_URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    if WEATHER_API_KEY is None:
        print("API key not installed")
        return

    params = {
        "key": WEATHER_API_KEY,
        "q": FILTERING
    }
    result = requests.get(BASE_URL, params=params)
    if result.status_code == 200:
        print(result.json())
    else:
        print(f"Error: {result.status_code}, {result.text}")


if __name__ == "__main__":
    get_weather()
