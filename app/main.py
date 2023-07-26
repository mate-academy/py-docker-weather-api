import os
import requests

from dotenv import load_dotenv


load_dotenv()
BASIC_URL = os.getenv("BASIC_URL")
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(f"{BASIC_URL}/current.json", {
        "key": API_KEY,
        "q": CITY
    })
    if response.status_code == 200:
        data = response.json()
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        temperature = data["current"]["temp_c"]
        temp_last_update = data["current"]["last_updated"]

        print(f"The weather in {CITY} is {condition.lower()}. "
              f"The temperature is {temperature} Celsius, "
              f"humidity - {humidity} "
              f"(last update: {temp_last_update}).")
    else:
        print("Cannot retrieve information.")


if __name__ == "__main__":
    get_weather()
