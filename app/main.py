import os

import requests


URL = "http://api.weatherapi.com/v1/current.json?"
AQI = "no"
API_KEY = os.getenv("API_KEY")
FILTERING = "Paris"


def get_weather() -> None:
    response = requests.get(URL + f"key={API_KEY}&q={FILTERING}&aqi={AQI}")
    location = response.json()["location"]
    current = response.json()["current"]

    name = location["name"]
    country = location["country"]
    localtime = location["localtime"]

    temp = current["temp_c"]
    condition = current["condition"]["text"]

    print(
        f"{name}/{country} {localtime} "
        f"Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
