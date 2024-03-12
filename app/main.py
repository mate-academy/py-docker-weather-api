import os
import requests


API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}
    res = requests.get(url=URL, params=params).json()
    print(res)


if __name__ == "__main__":
    get_weather()
