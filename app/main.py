import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:

    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("Error: API key not provided.")
        return
    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no",
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Current weather in: {city}, {country}")
    print(f"Current weather temperature: {temp_c}")
    print(f"Current weather condition: {condition}")


if __name__ == "__main__":
    get_weather()
