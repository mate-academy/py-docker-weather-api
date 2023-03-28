import os
from dotenv import load_dotenv
import requests

load_dotenv()
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(f"{URL}key= {API_KEY}&q={FILTERING}")
    response = response.json()
    location = response["location"]
    current = response["current"]

    print(f"{location['name']}/{location['country']} "
          f"{location['localtime']} "
          f"Weather: {current['temp_c']} Celsius, "
          f"{current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
