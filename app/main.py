import os

import requests

API_KEY = os.environ.get("API_KEY")

BASE_URL = "https://api.weatherapi.com/v1"


def get_weather(location: str, aqi: bool = True) -> dict:
    params = {
        "key": API_KEY,
        "q": location,
        "aqi": "yes" if aqi else "no",
    }

    response = requests.get(f"{BASE_URL}/current.json", params=params)

    return response.json()


if __name__ == "__main__":
    print(get_weather("Eindhoven", True))
