import os
import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    url = (
        f"{BASE_URL}?"
        f"key={API_KEY}&q={CITY}&aqi=no"
    )
    if not API_KEY:
        print("Error: API_KEY environment variable is not set.")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in {CITY}: {temp_c}°C, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")


if __name__ == "__main__":
    get_weather()
