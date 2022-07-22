import requests

from pprint import pprint

import os


def get_weather():
    os.environ["API_KEY"] = "b45afc4e7b2a4bf9a02151752222107"
    api_key = os.environ.get("API_KEY")
    request_data = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris").json()
    pprint(request_data)


if __name__ == "__main__":
    get_weather()
