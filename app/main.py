import os

import requests
from dotenv import load_dotenv

load_dotenv()
URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print_weather_info(data)
    else:
        print(f"Error: {response.status_code} - {response.text}")


def print_weather_info(weather: dict) -> None:
    location = weather["location"]
    current = weather["current"]

    print(
        f"Weather in {location['name']}, "
        f" {location['region']}, {location['country']}: "
        f" Local Time: {location['localtime']}"
        f" Temperature: {current['temp_c']}°C ({current['temp_f']}°F)"
        f" Wind: {current['wind_kph']} kph, "
        f" Humidity: {current['humidity']}%"
        f" UV Index: {current['uv']}"
        f" Cloud Cover: {current['cloud']}%"
        f" Feels Like: {current['feelslike_c']}°C ({current['feelslike_f']}°F)"
    )


if __name__ == "__main__":
    get_weather()
