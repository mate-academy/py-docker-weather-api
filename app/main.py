import os

import requests


API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(api_key: str, location: str = "London") -> None:
    params = {
        "key": api_key,
        "q": location,
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    data = response.json()
    current_weather = data["current"]

    print(f"Current weather in {location}: ")
    print(f"Temperature: {current_weather['temp_c']}C")
    print(f"Wind: {current_weather['wind_kph']}km/h")


if __name__ == "__main__":
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        raise ValueError("No API key provided")

    get_weather(API_KEY)
