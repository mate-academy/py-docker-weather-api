import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
COUNTRY = "France"
URL = f"{BASE_URL}?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            weather_data = response.json()
            condition = weather_data["current"]["condition"]["text"]
            temp_c = weather_data["current"]["temp_c"]
            time = weather_data["location"]["localtime"]
            print(f"{CITY}/{COUNTRY} {time}"
                  f"Weather: {temp_c} Celsius, {condition}")
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    get_weather()
