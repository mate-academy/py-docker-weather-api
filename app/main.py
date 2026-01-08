import os
import sys
import requests


BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
AQI_OPTION = "no"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        print("API_KEY environment variable is not set.")
        sys.exit(1)

    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": AQI_OPTION
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Current weather in {CITY}: {temp}°C, {condition}")


if __name__ == "__main__":
    get_weather()
