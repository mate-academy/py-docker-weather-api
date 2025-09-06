# app/main.py
import os
from dotenv import load_dotenv
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
DEFAULT_CITY = "Paris"
AQI_PARAM = "no"


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set")

    city = DEFAULT_CITY
    url = f"{BASE_URL}?q={city}" f"&key={api_key}" f"&aqi={AQI_PARAM}"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    temp = data["current"]["temp_c"]
    description = data["current"]["condition"]["text"]
    print(f"Current weather in {city}: {temp}°C, {description}")


if __name__ == "__main__":
    get_weather()
