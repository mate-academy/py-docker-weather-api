import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json?"
LOCATION = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    payload = {
        "key": API_KEY,
        "q": LOCATION
    }
    result = requests.get(URL, params=payload).json()
    city = result["location"]["name"]
    country = result["location"]["country"]
    localtime = result["location"]["localtime"]
    temp_c = result["current"]["temp_c"]
    air_condition = result["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...")
    print(f"{city}/{country} {localtime} "
          f"Weather: {temp_c} Celsius, {air_condition}")


if __name__ == "__main__":
    get_weather()
