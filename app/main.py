import os
import requests
from dotenv import (
    load_dotenv,
)

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    response = requests.get(URL)
    data = response.json()

    condition = data["current"]["condition"]["text"]
    temp = data["current"]["temp_c"]
    print(f"Weather in {CITY}: {condition}, {temp}°C")


if __name__ == "__main__":
    get_weather()
