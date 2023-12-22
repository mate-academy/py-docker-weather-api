import os
import requests
from dotenv import load_dotenv


load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:

    payload = {
        "key": API_KEY,
        "q": CITY
    }

    response = requests.get(URL, payload)
    weather_info = response.json()

    if response.status_code == 200:
        city_name = weather_info["location"]["name"]
        country_name = weather_info["location"]["country"]
        local_time = weather_info["location"]["localtime"]
        temp_c = weather_info["current"]["temp_c"]
        weather_condition = weather_info["current"]["condition"]["text"]

        print(f"Performing request to Weather API for city {CITY}...")
        print(
            f"{city_name}/{country_name} "
            f"{local_time} Weather: {temp_c} Celsius, {weather_condition}"
        )

    else:
        print(f"Something wrong...Error code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
