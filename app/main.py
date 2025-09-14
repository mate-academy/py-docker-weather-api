import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    response = requests.get(
        url="https://api.weatherapi.com/v1/current.json",
        params={"key": os.getenv("API_KEY"), "q": "Paris"},
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


if __name__ == "__main__":
    get_weather()
