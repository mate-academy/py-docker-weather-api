import os
from dotenv import load_dotenv
import requests

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
KEY = os.environ.get("API_KEY")
FILTERING = {
    "q": "Paris",
    "key": KEY
}
HEADERS = {
    "Accept": "application/json",
}


def get_weather() -> None:
    return requests.get(url=URL, params=FILTERING, headers=HEADERS).json()


if __name__ == "__main__":
    print(get_weather())
