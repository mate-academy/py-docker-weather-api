import os
import sys
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"

def get_weather(city: str) -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("API_KEY not found")
        sys.exit(1)
    params = {"key": api_key, "q": city, "aqi": "no"}
    try:
        resp = requests.get(BASE_URL, params=params)
        resp.raise_for_status()  # якщо код != 200, буде виняток
        data = resp.json()
        temp = data["current"]["temp_c"]
        print(f"Temperature in {city}: {temp}°C")
    except requests.exceptions.RequestException as e:
        print("API error:", e)


if __name__ == "__main__":
    get_weather()
