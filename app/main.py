import os

import requests

from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    API_KEY = os.environ.get("API_KEY")
    BASE_URL = "https://api.weatherapi.com/v1/current.json"

    response = requests.get(BASE_URL, params={
        "key": API_KEY,
        "q": "Paris",
    })

    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Temperature in {location}, {country} is {temp_c}, {condition}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    get_weather()
