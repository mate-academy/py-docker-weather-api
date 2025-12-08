import requests
import os

API_KEY = os.getenv("API_KEY")


def get_weather():
    URL = "http://api.weatherapi.com/v1/current.json"
    FILTERING = "Paris"

    params = {"key": API_KEY, "q": FILTERING}

    result = requests.get(URL, params=params)

    return result.json()


if __name__ == "__main__":
    get_weather()
