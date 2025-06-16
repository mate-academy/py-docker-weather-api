import os
import requests
from dotenv import load_dotenv


load_dotenv()

BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:

    params = {
        "key": API_KEY,
        "q": "Paris",
        "aqi": "no"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Weather in {location}({country}): {temp_c}°C, {condition}")
    else:
        print("Error", response.status_code, response.text)


if __name__ == "__main__":
    get_weather()
