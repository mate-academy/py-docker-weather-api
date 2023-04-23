import json
import os

import requests
from dotenv import load_dotenv


load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
LOCATION = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": LOCATION}
    response = requests.get(URL, params=params)
    data = response.json()
    print(json.dumps(data, indent=4))


if __name__ == "__main__":
    get_weather()
