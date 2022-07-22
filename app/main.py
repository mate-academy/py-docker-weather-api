import requests

from pprint import pprint

import os


def get_weather():
    api_key = os.environ.get("API_KEY")
    request_data = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris").json()
    pprint(request_data)


if __name__ == "__main__":
    get_weather()
