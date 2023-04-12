import os

import requests

API_KEY = os.getenv("API_KEY")
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&"
FILTERING = "Paris"


def get_weather() -> None:
    response = requests.get(URL + f"q={FILTERING}")
    data = response.json()

    weather_place = data["location"]["name"]
    country = data["location"]["country"]
    date = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    output = (
        f"{weather_place}/{country} {date} Weather:"
        f" {temperature} Celsius, {condition}"
    )

    print(output)


if __name__ == "__main__":
    get_weather()
