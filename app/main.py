import os
import requests
from dotenv import load_dotenv


load_dotenv()
URL = "https://api.weatherapi.com/v1/current.json"
KEY = os.environ["API_KEY"]


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = requests.get(URL, params={"key": KEY, "q": "Paris"})
    response_json = response.json()
    location = response_json["location"]
    current = response_json["current"]
    print(f"{location['name']}/{location['country']} "
          f"{location['localtime']} "
          f"Weather: {current['temp_c']} Celsius, "
          f"{current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
