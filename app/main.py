import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.environ["API_KEY"]
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
PAYLOAD = {"key": API_KEY, "q": CITY}


def get_weather() -> None:

    res = requests.get(URL, params=PAYLOAD).json()

    print(f"Performing request to Weather API for city {CITY}..."
          f"{res['location']['name']}/{res['location']['country']} "
          f"{res['location']['localtime']} Weather: "
          f"{res['current']['temp_c']} Celsius, "
          f"{res['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
