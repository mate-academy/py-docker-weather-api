import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("API_KEY is required")
    sys.exit(1)

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    print(f"Weather API for city {CITY}...")

    response = requests.get(
        url=URL,
        params={
            "key": API_KEY,
            "q": CITY
        }
    )

    if response.status_code != 200:
        print(f"Error from API: {response.text}")
        sys.exit(1)

    data = response.json()
    location = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        f"{location}/{country} {localtime} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
