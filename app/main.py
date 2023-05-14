import os

import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        url=BASE_URL, params={"q": CITY, "key": API_KEY}
    ).json()

    temp_c = response["current"]["temp_c"]
    text = response["current"]["condition"]["text"]
    last_update = response["current"]["last_updated"]

    print(f"In {CITY} for {last_update} is {text}"
          f" and temperature is {temp_c}°")


if __name__ == "__main__":
    get_weather()
