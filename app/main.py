import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()
KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

if not KEY:
    print("API_KEY is not set")
    sys.exit(1)


def get_weather() -> None:

    params = {
        "key": KEY,
        "q": CITY,
    }

    try:
        result = requests.get(URL, params=params)
        result.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    try:
        data = result.json()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)



    print(f"{data['location']['name']} - {data['current']['temp_c']}")


if __name__ == "__main__":
    get_weather()
