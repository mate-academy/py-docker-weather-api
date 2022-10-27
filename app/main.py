import os

import requests
from dotenv import load_dotenv

load_dotenv()

KEY = os.environ.get("API_KEY")
CITY = "Paris"
API_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:

    response = requests.get(
        API_URL,
        params={"key": {KEY}, "q": {CITY}}
    )

    if response.status_code == 200:
        info = response.json()

        print(
            f"{info['location']['country']}/{info['location']['name']} "
            f"{info['location']['localtime']} "
            f"Weather: {info['current']['temp_c']} Celsius, "
            f"{info['current']['condition']['text']}"
        )

    print("You need to check your API_URL, KEY and CITY")


if __name__ == "__main__":
    get_weather()
