import os
import requests
from typing import Any, Dict


BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY_ENV_NAME = "API_KEY"
REQUEST_TIMEOUT_SECONDS = 10


def _get_api_key() -> str:
    api_key = os.getenv(API_KEY_ENV_NAME)
    if not api_key:
        raise ValueError(
            f"{API_KEY_ENV_NAME} environment variable is not set. "
            "Pass it to the container with: -e API_KEY=your_key"
        )
    return api_key


def get_weather() -> None:
    api_key = _get_api_key()

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(
        BASE_URL,
        params={"key": api_key, "q": CITY, "aqi": "no"},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()

    weather_data: Dict[str, Any] = response.json()

    location = weather_data["location"]
    current = weather_data["current"]

    city_name = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    temperature_c = float(current["temp_c"])
    condition = current["condition"]["text"]

    print(
        f"{city_name}/{country} {localtime} "
        f"Weather: {temperature_c: .1f} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
