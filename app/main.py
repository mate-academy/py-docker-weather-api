import os

import requests
from dotenv import load_dotenv


load_dotenv()

CITY = "Paris"
API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:

    message = f"Performing request to Weather API for city {CITY}..."
    params = {
        "key": API_KEY,
        "q": CITY
    }

    print(message)

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        response = response.json()

        location_object = response["location"]
        weather_object = response["current"]

        location_data = (
            f"{location_object['name']}/{location_object['country']} "
            f"{location_object['localtime']}"
        )
        weather_data = (
            f"Weather: {weather_object['temp_c']} Celsius, "
            f"{weather_object['condition']['text']}"
        )

        print(location_data, weather_data)
    else:
        print("Invalid API_KEY or CITY")


if __name__ == "__main__":
    get_weather()
