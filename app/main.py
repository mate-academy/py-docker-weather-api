import os

import requests

endpoint = "https://api.weatherapi.com/v1/current.json"
api_key = os.environ.get("API_KEY")
city = "Paris"


def get_weather():
    weather_params = {
        "key": api_key,
        "q": city
    }
    response = requests.get(endpoint, params=weather_params).json()

    weather_condition = response["current"]["condition"]["text"].lower()
    temperature = response["current"]["temp_c"]
    winds = response["current"]["wind_mph"]

    print(f"Performing request to the Weather API...\n"
          f"Currently is {weather_condition} in {city}"
          f" and the temperature is {temperature} ºC with"
          f" {winds} mph winds.")


if __name__ == "__main__":
    get_weather()
