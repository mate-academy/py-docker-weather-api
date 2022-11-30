import os

import requests

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "PARIS"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL, params={
        "key": API_KEY, "q": FILTERING
    }).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    local_time = response["location"]["localtime"]
    weather = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...")
    print(f"{city}/{country} {local_time} "
          f"Weather: {weather} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
