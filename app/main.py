import os

from dotenv import load_dotenv

import requests


load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    weather_url = "http://api.weatherapi.com/v1"
    current_weather = "/current.json"
    url = f"{weather_url}{current_weather}?key={API_KEY}&q={CITY}"
    response = requests.get(url).json()
    print("Performing request to Weather API for city " + CITY)
    if requests.get(url).status_code == 200:
        print(f"{CITY}/{response['location']['country']} "
              f"{response['location']['localtime']} "
              f"Weather: {response['current']['temp_c']} Celsius, "
              f"{response['current']['condition']['text']}")
    else:
        print(f"HTTP status code's Error.")


if __name__ == "__main__":
    get_weather()
