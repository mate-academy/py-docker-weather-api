import os
import requests
from dotenv import load_dotenv


load_dotenv()

CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print(f"Current Weather in {CITY} "
              f"({weather_data['location']['localtime']}):")
        print(f"It is {weather_data['current']['condition']['text']} now")
        print(f"Temperature: {weather_data['current']['temp_c']} Celsius")
    else:
        print("Could not fetch weather")


if __name__ == "__main__":
    get_weather()
