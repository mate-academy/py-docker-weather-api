from datetime import datetime
import os
import requests
import sys

from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
FRILTERING = "Paris"

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("API key not found. Please set the API_KEY environment variable.")
    sys.exit(1)

def get_weather() -> None:
    try:
        resp = requests.get(URL, params={
            "key": API_KEY,
            "q": FRILTERING,
        })
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return

    data = resp.json()
    current = data.get("current")
    if not current:
        print("No current weather data found.")
        return
    
    print(f"Paris/France {datetime.now():%Y-%m-%d %H:%M} Weather: {current['temp_c']} Celsius, {current['condition']['text']}")

if __name__ == "__main__":
    get_weather()
