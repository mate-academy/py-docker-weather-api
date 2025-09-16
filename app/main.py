import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    try:
        response = requests.get(
            url=API_URL,
            params={"key": os.getenv("API_KEY"), "q": CITY},
        )

        data = response.json()

        location = data.get("location", {})
        current = data.get("current", {})
        condition = current.get("condition", {})

        city = location.get("name", "Unknown")
        country = location.get("country", "Unknown")
        localtime = location.get("localtime", "Unknown")
        temp_c = current.get("temp_c", "Unknown")
        condition_text = condition.get("text", "Unknown")

        print(f"{city}/{country} {localtime} "
              f"Weather: {temp_c} Celcius, {condition_text}")
    except Exception:
        raise


if __name__ == "__main__":
    get_weather()
