import os

import requests

from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    base_url = "https://api.weatherapi.com/v1/current.json"

    response = requests.get(base_url, params={
        "key": api_key,
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
