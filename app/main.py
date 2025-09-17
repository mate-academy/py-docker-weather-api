import os
import sys

import requests
from dotenv import load_dotenv


load_dotenv()


URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API Key is missing")
        sys.exit(1)
    try:
        response = requests.get(URL + f"key={api_key}&q={FILTERING}")
        response.raise_for_status()
        response_json = response.json()
        country = response_json["location"]["country"]
        city = response_json["location"]["name"]
        location = (f"{city}/"
                    f"{country}")
        time = response_json["location"]["localtime"]
        weather = (f"Weather: {response_json['current']['temp_c']} Celsius, "
                   f"{response_json['current']['condition']['text']}")
        print(f"{location} {time} {weather}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
