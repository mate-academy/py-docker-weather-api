import os

import requests
from dotenv import load_dotenv

load_dotenv()


def perform_request() -> dict:
    payload = {
        "q": "Paris"
    }
    headers = {"key": os.environ["API_KEY"]}
    url = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(url, params=payload, headers=headers).json()
    return response


def parse_response(response: dict) -> str:
    response = perform_request()
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
