import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"
    response = requests.get(url)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    print(get_weather())
