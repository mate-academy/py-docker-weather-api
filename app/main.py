import requests
import os

API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather() -> None:
    URL = "http://api.weatherapi.com/?"
    FILTERING = "Kyiv"

    params = {"key": API_KEY, "city": FILTERING}

    result = requests.get(URL, params=params)


if __name__ == "__main__":
    get_weather()
