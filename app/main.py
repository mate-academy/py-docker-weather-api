import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        return

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in {CITY}: {temp}°C, {condition}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
