import os

import requests

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:

    r = requests.get(url=URL, params={"key": API_KEY, "q": FILTERING})
    print("Performing request to Weather API for city Paris...")
    if r.status_code != 200:
        print(f"Request error, Status code: {r.status_code} != 200")
        return
    data = r.json()
    print(f'{data["location"]["name"]}'
          f'/{data["location"]["country"]}'
          f' {data["location"]["localtime"]}'
          f' Weather: {data["current"]["temp_c"]} Celsius,'
          f' {data["current"]["condition"]["text"]}')


if __name__ == "__main__":
    get_weather()
