import os

import requests
from dotenv import load_dotenv

load_dotenv()

CITY = "Paris"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"


def perform_request() -> dict:
    payload = {
        "q": CITY
    }
    key_api = os.getenv("API_KEY")
    if key_api is None:
        raise ValueError("API_KEY isn't set!")
    headers = {"key": key_api}
    response = requests.get(
        WEATHER_API_URL,
        params=payload,
        headers=headers
    ).json()
    return response


def parse_response(response: dict) -> str:
    city = response["location"]["name"]
    country = response["location"]["country"]
    local_time = response["location"]["localtime"]
    temp = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]
    message = (
        f"{city}/{country} {local_time} Weather: "
        f"{temp} Celsius, {condition}"
    )
    return message


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = perform_request()
    message = parse_response(response)
    print(message)


if __name__ == "__main__":
    get_weather()
