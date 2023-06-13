import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["WEATHER_API_KEY"]

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    payload = {"key": API_KEY, "q": "Paris"}
    response = requests.get(WEATHER_API_URL, params=payload)
    print(response.text)


if __name__ == "__main__":
    get_weather()
