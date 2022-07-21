import os

import requests


WEATHER_ENDPOINT = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("WEATHER_API_KEY")
CITY = "Paris"

params = {
    "key": API_KEY,
    "q": CITY,
}


def get_weather():
    response = requests.get(WEATHER_ENDPOINT, params=params)
    data = response.json()
    location_data = data["location"]

    location = f"{location_data['name']}/{location_data['country']}"
    localtime = location_data["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print("Performing request to Weather API for city Paris...")
    print(f"{location} {localtime} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
