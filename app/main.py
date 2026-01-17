import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")
if API_KEY is None:
    print("API_KEY not provided")
    sys.exit(1)
CITY = "Paris"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    payload = {"key": API_KEY, "q": CITY}
    try:
        res = requests.get(WEATHER_API_URL, params=payload)
        res.raise_for_status()
        data = res.json()
        print(
            f"{data['location']['name']}/{data['location']['country']}"
            f" {data['location']['localtime']}"
            f" Weather: {data['current']['temp_c']}"
            f" Celsius, {data['current']['condition']['text']}"
        )
    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_weather()
