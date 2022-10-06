import os

import requests

ENDPOINT = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather():
    weather_params = {
        "key": API_KEY,
        "q": CITY,
    }
    response = requests.get(ENDPOINT, params=weather_params).json()

    weather_condition = response["current"]["condition"]["text"].lower()
    temperature = response["current"]["temp_c"]
    winds = response["current"]["wind_mph"]

    print(f"Performing request to the Weather API...\n"
          f"Currently is {weather_condition} in {CITY}"
          f" and the temperature is {temperature} ºC with"
          f" {winds} mph winds.")


if __name__ == "__main__":
    get_weather()
