import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        location = weather_data["location"]["name"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]

        print(f"Weather in {location}:\nTemperature: {temperature}\n"
              f"Condition: {condition}")
    else:
        print(f"Error: {response.status_code} -> {response.text}")


if __name__ == "__main__":
    get_weather()
