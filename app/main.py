import os

import requests
from dotenv import load_dotenv


load_dotenv()

CITY = "Paris"
BASE_URL = "https://api.weatherapi.com/v1"
REQUEST_URL = f"{BASE_URL}/current.json?q={CITY}"
API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise Exception("Provide WeatherAPI API_KEY")


def get_weather() -> None:
    response = requests.get(
        REQUEST_URL,
        headers={
            "key": API_KEY,
        }
    )

    return response.json()


if __name__ == "__main__":
    get_weather()
