import os
from dotenv import load_dotenv

import requests

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")

    result = requests.get(URL, params={"key": API_KEY, "q": FILTERING}).json()

    city = result["location"]["name"]
    country = result["location"]["country"]
    local_time = result["location"]["localtime"]
    temp_c = result["current"]["temp_c"]
    condition = result["current"]["condition"]["text"]

    print(
        f"{city}/{country} {local_time} Weather: {temp_c} Celsius, {condition}"
    )
    pass


if __name__ == "__main__":
    get_weather()
