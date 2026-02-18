import requests
import os
from dotenv import load_dotenv

load_dotenv()
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise SystemExit("API_KEY not set")


def get_weather(city: str) -> None:
    params = {
        "key": API_KEY,
        "q": city
    }
    response = requests.get(URL, params=params)
    data = response.json()
    print(data["current"]["temp_c"])
    print(data["current"]["condition"]["text"])


if __name__ == "__main__":
    get_weather(CITY)
