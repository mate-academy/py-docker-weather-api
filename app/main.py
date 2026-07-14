import os
import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"

if API_KEY is None:
    raise ValueError("API_KEY environment variable is not set")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": "Paris",
        "aqi": "no",
    }

    response = requests.get(BASE_URL, params=params)
    print(response.json())


if __name__ == "__main__":
    get_weather()
