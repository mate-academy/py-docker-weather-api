import os
import sys

import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    print("API_KEY is missing.")
    sys.exit()

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def validate_field(field: str, data: dict) -> bool:
    return data.get(field) is not None


def validate_weather_info(data: dict) -> bool:
    for field in ("location", "current"):
        if not validate_field(field, data):
            return False

    for field in ("name", "country", "localtime"):
        if not validate_field(field, data["location"]):
            return False

    for field in ("temp_c", "condition"):
        if not validate_field(field, data["current"]):
            return False

    for field in ("text", ):
        if not validate_field(field, data["current"]["condition"]):
            return False

    return True


def print_weather_info(data: dict) -> None:
    if not validate_weather_info(data):
        print("Weather info is invalid")
        sys.exit()
    location = data["location"]
    current = data["current"]
    condition = current["condition"]

    print(
        f'{location["name"]}/{location["country"]} '
        f'{location["localtime"]} Weather: '
        f'{current["temp_c"]} Celsius, {condition["text"]}'
    )


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = requests.get(
        url=URL,
        params={
            "key": API_KEY,
            "q": FILTERING,
            "lang": "en"
        }
    )
    if response.status_code != 200:
        print(f"Response status code: {response.status_code}")
        if response.text:
            print(f"Response info: {response.text}")
        sys.exit()

    print_weather_info(response.json())


if __name__ == "__main__":
    get_weather()
