import os

import requests


CITY = "Kiev"


def get_weather() -> None:
    key = os.getenv("API_KEY")
    url = "https://api.weatherapi.com/v1/current.json"

    params = {"key": key, "q": CITY}

    response = requests.get(url, params=params)
    result = response.json()
    location = result["location"]
    current = result["current"]
    print(f"{location['name']}/{location['country']} {location['localtime']}"
          f" Weather: {current['temp_c']} Celsius, "
          f"{current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
