import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY_ENV = "API_KEY"
TIMEOUT = 10


def get_weather() -> None:
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        raise ValueError("API_KEY is not set in environment variables")

    response = requests.get(
        BASE_URL,
        params={"key": api_key, "q": CITY},
        timeout=TIMEOUT,
    )
    response.raise_for_status()

    data = response.json()
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Weather in {CITY}: {condition}, {temp_c}°C")


if __name__ == "__main__":
    get_weather()
