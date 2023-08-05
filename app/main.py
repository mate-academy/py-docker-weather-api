import os

import requests

from dotenv import load_dotenv

load_dotenv()


REQUEST_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        REQUEST_URL,
        params={"key": API_KEY, "q": "Paris"})

    city = response.json()["location"]["name"]
    country = response.json()["location"]["country"]
    localtime = response.json()["location"]["localtime"]
    temperature = response.json()["current"]["temp_c"]
    condition = response.json()["current"]["condition"]["text"]

    print(f"{city}/{country} {localtime} "
          f"Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
