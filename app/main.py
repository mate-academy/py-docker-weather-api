import os
from time import sleep

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(URL + f"key={API_KEY}&q={CITY}")
    if response.status_code == 200:
        result = response.json()
        print(f"Performing request for Weather Api for city {CITY}...")
        sleep(1)
        print(
            f'{CITY}/{result["location"]["country"]}'
            f' {result["location"]["localtime"]}'
            f' Weather: {result["current"]["temp_c"]}'
            f' Celsius, {result["current"]["condition"]["text"]}'
        )
    else:
        print("your API_KEY is wrong or Weather site unavailable")


if __name__ == "__main__":
    get_weather()
