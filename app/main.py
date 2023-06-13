import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["WEATHER_API_KEY"]


def get_weather() -> None:
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}=Paris"
    response = requests.get(url)
    print(response.text)


if __name__ == "__main__":
    get_weather()
