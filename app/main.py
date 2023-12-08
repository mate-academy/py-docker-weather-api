import os
from dotenv import load_dotenv

import requests

load_dotenv()
URL = "https://api.weatherapi.com/v1/current.json"
my_key = os.environ["API_KEY"]


def get_weather() -> None:
    result = requests.get(URL + f"?q=Paris&key={my_key}").json()
    city = result["location"]["name"]
    country = result["location"]["country"]
    localtime = result["location"]["localtime"]
    temperature = result["current"]["temp_c"]
    weather = result["current"]["condition"]["text"]
    print(f"{city}/{country} {localtime} "
          f"Weather: {temperature} Celsius, {weather}")


if __name__ == "__main__":
    get_weather()
