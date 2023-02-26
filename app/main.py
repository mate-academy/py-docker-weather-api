import requests
from time import sleep
import os


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    URL = "http://api.weatherapi.com/v1/current.json?"
    CITY = "Paris"
    response = requests.get(URL, params={"key": API_KEY, "q": CITY})
    if response.status_code == 200:
        response = response.json()
        print(f"Performing request for Weather Api for city {CITY}...")
        sleep(1)
        print(
            f'{response["location"]["name"]}/'
            f'{response["location"]["country"]}'
            f' {response["location"]["localtime"]}'
            f' Weather: {response["current"]["temp_c"]}'
            f' Celsius, {response["current"]["condition"]["text"]}'
        )
    else:
        print("Please check your API_KEY and be sure it`s right")


if __name__ == "__main__":
    get_weather()
