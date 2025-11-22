import os
import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    print(data)


if __name__ == "__main__":
    get_weather()
