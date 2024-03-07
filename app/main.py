import os

import requests
from dotenv import load_dotenv

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    load_dotenv()
    req = requests.get(f"{URL}key={API_KEY}&q={FILTERING}")
    if req.status_code != 200:
        print("Something went wrong")
    else:
        data = req.json()
        print(f"Performing request to Weather API for city {FILTERING}...")
        print(f"{data['location']['name']}/{data['location']['country']} "
              f"{data['location']['localtime']} "
              f"Weather: {data['current']['temp_c']} Celsius, "
              f"{data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
