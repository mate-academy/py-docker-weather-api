import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
CITY_NAME = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY_NAME}...")
    params = {"key": f"{API_KEY}", "q": CITY_NAME, "aqi": "no"}
    response = requests.get(WEATHER_API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(
            f'{params["q"]}/'
            f'{data["location"]["country"]} '
            f'{data["location"]["localtime"]} '
            f'Weather: {data["current"]["temp_c"]}°C, '
            f'{data["current"]["condition"]["text"]}'
        )


if __name__ == "__main__":
    get_weather()
