import os

import requests


WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY_ENVIRONMENT_VARIABLE = "API_KEY"
REQUEST_TIMEOUT_SECONDS = 10


def get_weather() -> None:
    api_key = os.getenv(API_KEY_ENVIRONMENT_VARIABLE)
    if not api_key:
        raise RuntimeError(
            f"{API_KEY_ENVIRONMENT_VARIABLE} environment variable is not set"
        )

    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(
        WEATHER_API_URL,
        params={"key": api_key, "q": CITY},
        timeout=REQUEST_TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    weather_data = response.json()

    location = weather_data["location"]
    current_weather = weather_data["current"]
    city = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    temperature = current_weather["temp_c"]
    condition = current_weather["condition"]["text"]

    print(
        f"{city}/{country} {localtime} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
