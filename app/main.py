import os

import requests


CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"
KEY = os.getenv("API_KEY")

def get_weather() -> None:
    params = {"key": KEY, "q": CITY}
    response = requests.get(URL, params=params)
    result = response.json()
    location = result["location"]
    current = result["current"]
    print(f"{location['name']}/{location['country']} {location['localtime']}"
          f" Weather: {current['temp_c']} Celsius, "
          f"{current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
