import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")

PARAMS = {"key": API_KEY, "q": FILTERING}


def get_weather() -> None:
    weather_response = requests.get(URL, params=PARAMS)
    w_rj = weather_response.json()

    temperature_celsius = w_rj["current"]["temp_c"]
    location_name = w_rj["location"]["name"]
    location_region = w_rj["location"]["country"]
    location_time = w_rj["location"]["localtime"]
    condition_text = w_rj["current"]["condition"]["text"]
    result = f"{location_name}/{location_region} {location_time} " \
             f"Weather: {temperature_celsius} Celsius, {condition_text}"
    print(result)


if __name__ == "__main__":
    get_weather()
