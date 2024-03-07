import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }
    response = requests.get(url=WEATHER_API_URL, params=params)
    print(response.json())


if __name__ == "__main__":
    get_weather()
