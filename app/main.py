import os

import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    response_json = requests.get(
        API_URL,
        params={"key": API_KEY, "q": CITY, "aqi": "no"}
    ).json()

    print("Performing request to weather API for city Paris...")

    location = response_json["location"]
    weather = response_json["current"]

    print(f"{location['name']}/{location['country']} "
          f"{weather['last_updated']} "
          f"Weather: {weather['temp_c']} Celsius, "
          f"{weather['condition']['text']}")


if __name__ == "__main__":
    get_weather()
