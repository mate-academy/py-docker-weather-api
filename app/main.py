import os
import requests

API_KEY = os.getenv("API_KEY")

CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        raise RuntimeError("API_KEY environment variable is not set")

    params = {
        "q": CITY,
        "key": API_KEY,
        "units": "metric"
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()

    data = response.json()

    temp = data["current"]["temp_c"]
    description = data["current"]["condition"]["text"]

    print(f"Current weather in {CITY}:")
    print(f"Temperature: {temp}°C")
    print(f"Description: {description}")


if __name__ == "__main__":
    get_weather()
