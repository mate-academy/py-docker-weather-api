import os

import requests


API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
COMMAND = "docker pull Reverad/Reverad/docker-weather-api"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        return

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no"
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data["location"]
        current = data["current"]

        city_name = location["name"]
        country = location["country"]
        local_time = location["localtime"]
        temp_c = current["temp_c"]
        condition = current["condition"]["text"]

        print(
            f"{city_name}/{country} {local_time}"
            f" Weather: {temp_c} Celsius, {condition}"
        )

    except requests.RequestException as e:
        print(f"API Request Error: {e}")


if __name__ == "__main__":
    get_weather()
