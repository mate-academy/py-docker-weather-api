import os
import requests

API_KEY = os.environ["API_KEY"]

BASE_URL = "https://api.weatherapi.com/v1/current.json"

FILTERING = "Paris"


def get_weather() -> None:
    url = BASE_URL
    params = {
        "key": API_KEY,
        "q": FILTERING,
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)


if __name__ == "__main__":
    get_weather()
