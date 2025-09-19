import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
AQI = "no"


def fetch_weather() -> dict:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is not set in environment variables")

    params = {"key": api_key, "q": CITY, "aqi": AQI}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()


def parse_weather(data: dict) -> tuple[str, float, str]:
    city = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    return city, temp_c, condition


def print_weather(city: str, temp_c: float, condition: str) -> None:
    print(f"Weather in {city}: {temp_c}°C, {condition}")


def get_weather() -> None:
    data = fetch_weather()
    city, temp_c, condition = parse_weather(data)
    print_weather(city, temp_c, condition)


if __name__ == "__main__":
    get_weather()
