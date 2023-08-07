import os

import requests

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    params = {
        "key": os.environ.get("API_KEY"),
        "q": FILTERING,
    }
    response = requests.get(url=URL, params=params)
    data = response.json()

    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {FILTERING}...")
    print(
        f"{country}/{FILTERING} {time} Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
