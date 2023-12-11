import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()

API_URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ["API_KEY"]


def get_weather() -> None:
    response = requests.get(
        API_URL + f"?key={API_KEY}&q={FILTERING}",
    )
    data = json.loads(response._content)
    city = data["location"]["name"]
    country = data["location"]["country"]
    datetime = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    weather = data["current"]["condition"]["text"]
    print(
        f"{city}/{country} {datetime} Weather:"
        f" {temperature} Celsius, {weather}"
    )


if __name__ == "__main__":
    print("Preforming request to Weather API for cite Paris...")
    get_weather()
