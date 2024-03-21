import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    res = requests.get(URL, params={"key": API_KEY, "q": CITY})

    if res.status_code == 200:
        location = res.json().get("location")
        weather = res.json().get("current")
        print(
            f"{location.get('name')}/{location.get('country')} "
            f"{weather.get('last_updated')} "
            f"Weather: {weather.get('temp_c')} Celsius, "
            f"{weather.get('condition').get('text')}"
        )
    else:
        print(
            "Something went wrong. "
            "Please check your passed data or try again later."
        )


if __name__ == "__main__":
    get_weather()
