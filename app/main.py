import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY_FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    payload = {"key": API_KEY, "q": CITY_FILTERING}
    res = requests.get(BASE_URL, params=payload)

    if res.status_code == 200:
        weather_dict = res.json()

        location = weather_dict["location"]["name"]
        last_updated = weather_dict["current"]["last_updated"]
        temp_c = weather_dict["current"]["temp_c"]
        humidity = weather_dict["current"]["humidity"]
        condition_text = weather_dict["current"]["condition"]["text"]

        print(f"Location: {location}")
        print(f"Condition: {condition_text}")
        print(f"Last updated: {last_updated}")
        print(f"Temperature: {temp_c} C")
        print(f"Humidity: {humidity} %")
    else:
        print(f"There is {res.status_code} error with your request")


if __name__ == "__main__":
    get_weather()
