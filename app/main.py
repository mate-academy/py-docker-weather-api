import requests

import os

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL, {
        "key": API_KEY,
        "q": CITY
    })

    result_data = response.json()

    city = result_data["location"]["name"]
    country = result_data["location"]["country"]
    localtime = result_data["location"]["localtime"]
    temperature = result_data["current"]["temp_c"]
    condition = result_data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...")

    if response.status_code == 200:
        print(
            f"{city}/{country} {localtime} "
            f"Weather: {temperature} Celsius, {condition}"
        )
    else:
        print(f"Error: {response.status_code}!!!")


if __name__ == "__main__":
    get_weather()
