import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"
KEY = os.getenv("API_KEY")


def get_weather() -> None:
    result = requests.get(URL + f"q={CITY}&key={KEY}")
    if result.status_code == 200:
        data = result.json()
        city = data["location"]["name"]
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        condition = data["current"]["condition"]["text"]
        full_info = (f"City: {city}, "
                     f"Temperature: {temp}, "
                     f"Humidity: {humidity}, "
                     f"Condition: {condition}")
        print(full_info)


if __name__ == "__main__":
    get_weather()
