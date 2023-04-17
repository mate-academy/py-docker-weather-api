import os
import requests
from dotenv import load_dotenv

load_dotenv()
REQUEST_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        REQUEST_URL,
        params={"key": API_KEY, "q": CITY}
    ).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    date = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...")
    print(
        f"{city}/{country} {date} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
