import os

import requests
from dotenv import load_dotenv

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY is not set. Please provide a valid API key.")
        return

    print(f"Performing request to Weather API for city {FILTERING}...")

    payload = {"key": api_key, "q": FILTERING}

    response = requests.get(
        URL,
        params=payload,
    )

    if response.status_code != 200:
        print(f"Error: Failed to fetch data from Weather API. "
              f"Status code: {response.status_code}")
        return

    result = response.json()

    location = result.get("location")
    current = result.get("current")

    if not location or not current or not current.get("condition"):
        print("Error: Incomplete data received from API.")
        return

    condition = current.get("condition")

    city = location.get("name")
    country = location.get("country")
    current_time = location.get("localtime")
    temperature = current.get("temp_c")
    weather = condition.get("text")

    print(f"{city}/{country} {current_time} "
          f"Weather: {temperature} Celsius, {weather}")


if __name__ == "__main__":
    get_weather()
