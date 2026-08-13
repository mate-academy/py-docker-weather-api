import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    params = {
        "key": api_key,
        "q": CITY,
    }

    print(f"Performing request to Weather API for city {CITY}...")
    response = requests.get(URL, params=params).json()

    location = response["location"]
    current = response["current"]

    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, {current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
