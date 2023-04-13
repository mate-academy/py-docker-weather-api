import os

import requests

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    result = requests.get(URL + f"key={API_KEY}&q={CITY}")
    data = result.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        f"{city}/{country} {time} Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
