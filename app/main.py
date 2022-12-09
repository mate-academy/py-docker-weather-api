import os

import requests as requests

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING
    }

    result = requests.get(URL, params).json()
    location = result["location"]["name"] + "/" + result["location"]["country"]
    date = result["current"]["last_updated"]
    weather = result["current"]["temp_c"]
    condition = result["current"]["condition"]["text"]
    print(f"{location} {date} {weather} Celsius,  {condition}")


if __name__ == "__main__":
    get_weather()
