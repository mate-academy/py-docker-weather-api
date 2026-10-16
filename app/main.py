import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING,
    }
    response = requests.get(URL, params=params)
    data = response.json()

    print(f"Paris: {data['current']['temp_c']}°C")


if __name__ == "__main__":
    get_weather()
