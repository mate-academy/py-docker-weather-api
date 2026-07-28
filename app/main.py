import os

import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    response = requests.get(
        BASE_URL,
        params={
            "key": api_key,
            "q": CITY,
        },
        timeout=10,
    )
    response.raise_for_status()

    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]
    wind = data["current"]["wind_kph"]

    print(f"Weather in {location}, {country}")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind: {wind} km/h")


if __name__ == "__main__":
    get_weather()
