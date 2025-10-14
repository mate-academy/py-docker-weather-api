import os
import sys
import requests


API_BASE_URL = "http://api.weatherapi.com/v1/current.json"
DEFAULT_CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    params = {"key": api_key, "q": DEFAULT_CITY}

    try:
        response = requests.get(API_BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}", file=sys.stderr)
        sys.exit(1)

    location = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location}/{country} {time} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
