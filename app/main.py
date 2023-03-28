import requests
import os
from dotenv import load_dotenv
load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
FILTERING = "paris"


def get_weather() -> None:

    weather_response = requests.get(URL + f"?key={API_KEY}&q={FILTERING}")

    temperature_celsius = weather_response.json()["current"]["temp_c"]
    location_name = weather_response.json()["location"]["name"]
    location_region = weather_response.json()["location"]["country"]
    location_time = weather_response.json()["location"]["localtime"]
    condition_text = weather_response.json()["current"]["condition"]["text"]

    result = f"{location_name}/{location_region} {location_time} " \
             f"Weather: {temperature_celsius} Celsius, {condition_text}"

    print(result)


if __name__ == "__main__":
    get_weather()
