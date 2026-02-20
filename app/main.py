import os
import sys
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API key not set")
        sys.exit(1)

    parameters = {
        "key": api_key,
        "q": "Paris"
    }

    response = requests.get(BASE_URL, params=parameters)
    if response.status_code != 200:
        print(f"Error getting weather. Problem: {response.text}")
        sys.exit(1)

    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{city}/{country} {localtime} Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
