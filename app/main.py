import os

import requests


api_key = os.environ.get("API_KEY")

BASE_URL = "https://api.weatherapi.com/v1/current.json?q=Paris&key="

URL = BASE_URL + api_key


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = requests.get(URL)
    json_data = response.json()
    city = json_data["location"]["name"]
    country = json_data["location"]["country"]
    localtime = json_data["location"]["localtime"]
    temp_c = json_data["current"]["temp_c"]
    condition = json_data["current"]["condition"]["text"]

    print(
        f"{city}/{country} {localtime} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
