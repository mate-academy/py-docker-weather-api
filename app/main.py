import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    city = "Paris"
    params = {
        'key': os.getenv('API_KEY'),
        'q': city,
        'aqi': 'yes'
    }
    response = requests.get(f"https://api.weatherapi.com/v1/current.json", params=params)
    weather_data = response.json()

    country_name = weather_data["location"]["country"]
    date_time = weather_data["location"]["localtime"]
    temperature_celsius = weather_data["current"]["temp_c"]
    temperature_fahrenheit = weather_data["current"]["temp_f"]
    weather = weather_data["current"]["condition"]["text"]
    print(
        f"Performing request to Weather API for city Paris...\n"
        f"City: {city}({country_name}) {date_time} {temperature_celsius}"
        f"°C ({temperature_fahrenheit}℉) {weather}"
    )


if __name__ == "__main__":
    get_weather()
