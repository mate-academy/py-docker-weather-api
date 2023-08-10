import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    payload = {"q": FILTERING, "key": "96a76300af1c4276a38192715231008"}
    response = requests.get(URL, params=payload)
    data = json.loads(response.text)
    print(
        f"Performing request to Weather API for city {FILTERING}... "
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['current']['last_updated']} "
        f"Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
