import os

import requests


API_KEY_ENV = "API_KEY"
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
REQUEST_TIMEOUT = 10


def get_weather() -> None:
    api_key = os.getenv(API_KEY_ENV)

    if not api_key:
        raise ValueError(f"{API_KEY_ENV} environment variable is required")

    response = requests.get(
        BASE_URL,
        params={"key": api_key, "q": CITY},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()

    weather = response.json()
    location = weather["location"]
    current = weather["current"]
    condition = current["condition"]["text"]
    location_name = location["name"]
    location_country = location["country"]
    temperature = current["temp_c"]
    feels_like = current["feelslike_c"]
    wind_speed = current["wind_kph"]
    humidity = current["humidity"]

    print(
        f"Weather in {location_name}, {location_country}: "
        f"{temperature} C, {condition}"
    )
    print(f"Feels like: {feels_like} C")
    print(f"Wind: {wind_speed} kph")
    print(f"Humidity: {humidity}%")


if __name__ == "__main__":
    get_weather()
