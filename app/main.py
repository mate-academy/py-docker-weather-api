import os
import sys
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
if not API_KEY:
    print("API_KEY is missing. Please set API_KEY.")
    sys.exit(1)

BASE_URL = "https://api.weatherapi.com/v1"
ENDPOINT_CURRENT = "/current.json"
CITY = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(
        url=BASE_URL + ENDPOINT_CURRENT,
        params={
            "key": API_KEY,
            "q": CITY,
        }
    )

    if response.status_code != 200:
        print("Cannot connect to the weather server.")
        sys.exit(1)

    data = response.json()

    location = data.get("location", {})
    city = location.get("name", "Unknown City")
    country = location.get("country", "Unknown Country")
    localtime = location.get(
        "localtime",
        datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    current = data.get("current", {})
    temp_c = current.get("temp_c", "NaN")
    condition = current.get("condition", {}).get("text", "")

    print(
        f"{city}/{country} {localtime} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
