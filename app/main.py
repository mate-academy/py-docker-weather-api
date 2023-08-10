import os
import requests


API_KEY = os.environ.get("WEATHER_API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/?"


def get_weather() -> str:
    response = requests.get(URL + f"key={API_KEY}&q={CITY}")
    data = response.json()

    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return (
        f"Current weather in {CITY}:"
        f" {description}, Temperature: {temperature}°C"
    )


if __name__ == "__main__":
    get_weather()
