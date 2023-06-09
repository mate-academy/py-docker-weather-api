import os
from dotenv import load_dotenv

import requests

load_dotenv()
BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:

    response = requests.get(
        url=BASE_URL, params={"q": CITY, "key": API_KEY}
    ).json()

    last_update = response["current"]["last_updated"]
    text = response["current"]["condition"]["text"]
    temp_c = response["current"]["temp_c"]
    wind = response["current"]["wind_kph"]
    wind_dir = response["current"]["wind_dir"]
    pressure_mb = response["current"]["pressure_mb"]
    humidity = response["current"]["humidity"]

    print(f"Weather report for {last_update}:")
    print(f"The weather in the {CITY} is {text}")
    print(f"The temperature is {temp_c} celsius.")
    print(f"The wind is {wind_dir}, speed {wind} km per hour.")
    print(f"Pressure: {pressure_mb} mb.")
    print(f"Humidity: {humidity}.")


if __name__ == "__main__":
    get_weather()