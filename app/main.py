import os
import requests

URL = "https://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ["API_KEY"]

CITY = "Paris"


def get_weather() -> str:
    response = requests.get(f"{URL}key={API_KEY}&q={CITY}")

    if response.status_code == 200:
        data = response.json()
        country = data["location"]["country"]
        time = data["location"]["localtime"]
        temp = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]
        print(f"Performing request to Weather API for city {CITY}...")
        print(f"{CITY}/{country} {time} Weather: {temp} Celsius, {weather}")

    return "Can't access to Weather_API"


if __name__ == "__main__":
    get_weather()
