import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    city = "Paris"
    text = requests.get(
        f"https://api.weatherapi.com/v1/current.json"
        f"?key={os.getenv('API_KEY')}&q={city}&aqi=yes"
    ).json()
    print(
        f"Now the weather in {city} is "
        f"{text['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
