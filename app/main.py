import os
from dotenv import load_dotenv
import requests

load_dotenv()

BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    params = {
        "key": api_key,
        "q": "Paris"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Weather in {city}, {country}: {temp_c}°C, {condition}")
    else:
        print("Something went wrong. Please try again")


if __name__ == "__main__":
    get_weather()
