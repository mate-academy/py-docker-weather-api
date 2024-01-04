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
        f"{location['region']}, {location['country']}:"
    )
    print(f"Local Time: {location['localtime']}")
    print(f"Temperature: {current['temp_c']}°C ({current['temp_f']}°F)")
    print(f"Condition: {current['condition']['text']}")
    print(
        f"Wind: {current['wind_kph']} kph, "
        f"{current['wind_degree']}° {current['wind_dir']}"
    )
    print(f"Humidity: {current['humidity']}%")
    print(f"Pressure: {current['pressure_mb']} mb")
    print(f"Visibility: {current['vis_km']} km")
    print(f"UV Index: {current['uv']}")
    print(f"Cloud Cover: {current['cloud']}%")
    print(
        f"Feels Like: {current['feelslike_c']}°C ({current['feelslike_f']}°F)"
    )


if __name__ == "__main__":
    get_weather()
