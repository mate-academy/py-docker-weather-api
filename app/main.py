import requests
import os

# To pull this image, use COMMAND = docker pull strauuch/weather-api

WEATHER_API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

def get_weather() -> None:

    if not WEATHER_API_KEY:
        print("Error: API_KEY is not set.")
        return


    url = f"{BASE_URL}?key={WEATHER_API_KEY}&q={CITY}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Paris/France 2026-02-28 00:00 Weather: {temp} Celsius, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        return

if __name__ == "__main__":
    get_weather()
