import os

import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URI = "http://api.weatherapi.com/v1/"
CITY = "Paris"


def get_weather() -> None:

    url = f"{BASE_URI}current.json?q={CITY}"
    params = {
        "key": API_KEY,
    }

    try:
        response = requests.get(url, params=params)

        response.raise_for_status()

        data = response.json()

    except requests.exceptions as err:
        print(err)

    city = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Performing request to weather API for city Paris...\n"
          f"{city}/{country} {time} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
