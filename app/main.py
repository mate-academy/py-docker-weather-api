import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
AQI = "no"


def get_weather() -> dict:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": AQI
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


def print_weather_summary(weather: dict) -> None:
    temp_c = weather["current"]["temp_c"]
    condition = weather["current"]["condition"]["text"]
    print(f"Weather in {CITY}: {temp_c}°C, {condition}")


if __name__ == "__main__":
    weather_data = get_weather()
    print_weather_summary(weather_data)
