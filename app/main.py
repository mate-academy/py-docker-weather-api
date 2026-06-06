import os

import requests


WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY_ENVIRONMENT_VARIABLE = "API_KEY"
REQUEST_TIMEOUT = 10


def get_weather() -> None:
    api_key = os.environ.get(API_KEY_ENVIRONMENT_VARIABLE)
    if not api_key:
        raise RuntimeError(
            f"{API_KEY_ENVIRONMENT_VARIABLE} environment variable is not set"
        )

    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(
        WEATHER_API_URL,
        params={"key": api_key, "q": CITY},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    weather_data = response.json()

    location = weather_data["location"]
    current_weather = weather_data["current"]
    condition = current_weather["condition"]["text"]

    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} Weather: "
        f"{current_weather['temp_c']} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
