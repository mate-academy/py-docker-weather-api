import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": "Paris"
    }

    res = requests.get(URL, params=params).json()

    country = res["location"]["country"]
    city = res["location"]["name"]
    date = res["location"]["localtime"]
    temp = res["current"]["temp_c"]

    print(
        f"{country} - {city}\n"
        f"Date: {date}\n"
        f"Temperature: {temp}"
    )


if __name__ == "__main__":
    get_weather()
