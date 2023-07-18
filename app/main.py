import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(URL, {
        "key": API_KEY,
        "q": CITY
    })

    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    wind_speed = data["current"]["wind_kph"]

    print(
        f"In {city} ({country}). "
        f"Air temperature: {temperature} Celsius. "
        f"Weather: {condition}. "
        f"Wind speed: {wind_speed} kph"
    )


if __name__ == "__main__":
    get_weather()
