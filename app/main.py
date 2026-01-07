import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json?"
KEY = os.getenv("API_KEY")
FILTERING = "Paris"


def get_weather() -> str | None:
    if not KEY:
        return "API_KEY is missing"
    print("Performing request to Weather API for city Paris...")

    response = requests.get(URL + f"key={KEY}&q={FILTERING}")
    response.raise_for_status()
    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{city}/{country} {localtime} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
