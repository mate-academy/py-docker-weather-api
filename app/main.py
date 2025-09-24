import os

import requests


WEATHER_API_KEY = os.getenv("API_KEY")
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:

    params = {
        "key": WEATHER_API_KEY,
        "q": CITY,
    }

    response = requests.get(WEATHER_API_URL, params=params)
    data = response.json()
    if response.status_code == 200:
        print(f"Performing request to Weather API for city {CITY} ...")
        print(f"{data['location']['name']}/{data['location']['country']} "
              f"{data['location']['localtime']} "
              f"Weather: {data['current']['temp_c']} Celsius, "
              f"{data['current']['condition']['text']}")
    else:
        print(response.status_code)


if __name__ == "__main__":
    get_weather()
