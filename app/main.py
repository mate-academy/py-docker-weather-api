import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    if API:
        result = requests.get(URL + f"key={API}&q={CITY}")
        temperature = result.json()["current"]["temp_c"]
        condition = result.json()["current"]["condition"]["text"]
        country = result.json()["location"]["country"]
        localtime = result.json()["location"]["localtime"]
        print(
            f"{CITY}/{country} {localtime} "
            f"Weather: {temperature} Celsius, {condition}"
        )
    return print("Please add API_KEY when run docker")


if __name__ == "__main__":
    URL = "http://api.weatherapi.com/v1/current.json?"
    CITY = "Paris"
    API = os.environ.get("API_KEY")
    get_weather()
