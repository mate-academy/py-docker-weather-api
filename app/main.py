import os
import sys
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
TARGET_CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    params = {
        "key": api_key,
        "q": TARGET_CITY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        city_name = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"{city_name}/{country} {local_time} "
              f"Weather: {temp_c} Celsius, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve weather data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
