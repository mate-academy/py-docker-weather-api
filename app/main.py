import os
from datetime import datetime
import requests

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"

WEATHER_API_URL = (
    f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
)


def get_weather() -> None:
    res = requests.get(WEATHER_API_URL)

    if res.status_code != 200:
        print(f"Error: Unable to get weather data. "
              f"HTTP Status Code: {res.status_code}")

    data = res.json()

    city = data["name"]
    country = data["sys"]["country"]
    timestamp = data["dt"]
    temperature = data["main"]["temp"] - 273.15
    weather = data["weather"][0]["description"]

    dt_object = datetime.fromtimestamp(timestamp)
    formatted_time = dt_object.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Performing request to Weather API for city {city}...")
    print(
        f"{city}/{country} {formatted_time} "
        f"Weather : {temperature:.1f} Celsius, {weather.capitalize()}"
    )


if __name__ == "__main__":
    get_weather()
