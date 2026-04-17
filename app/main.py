import os
import sys
import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
BASE_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY environment variable is not set.")
        sys.exit(1)

    url = f"{BASE_URL}?key={API_KEY}&q={CITY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in {CITY}: {temp}°C, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
