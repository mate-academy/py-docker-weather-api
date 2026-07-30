import os

import requests


WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    response = requests.get(
        url=WEATHER_API_URL,
        params={
            "key": api_key,
            "q": CITY,
        }
    )
    weather = response.json()
    print(weather["location"]["name"])
    print(weather["current"]["temp_c"])
    print(weather["current"]["condition"]["text"])


if __name__ == "__main__":
    get_weather()
