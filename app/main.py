import os
import sys
import requests

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY environment variable is not set")
        sys.exit(1)

    print(f"Performing request to Weather API for city {CITY}...")

    params = {
        "key": API_KEY,
        "q": CITY,
    }

    response = requests.get(URL, params=params)
    response.raise_for_status()
    data = response.json()

    location_name = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        f"{location_name}/{country} {local_time} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
