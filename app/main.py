import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(WEATHER_API_URL + f"?key={API_KEY}&q={CITY}")
    print(response.json())


if __name__ == "__main__":
    get_weather()
