import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("WEATHER_API_KEY")

    print(f"Performing request to Weather API for city {CITY}...")

    params = {"key": api_key, "q": CITY}

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        location = data["location"]
        current = data["current"]

        print(
            f"{location['name']}/{location['country']} "
            f"{location['localtime']} "
            f"Weather: {current['temp_c']} Celsius, "
            f"{current['condition']['text']}"
        )
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
