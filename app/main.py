import os

import requests


URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING,
        "aqi": "no"
    }

    result = requests.get(URL, params=params)
    data = result.json()
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} Weather: "
        f"{data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
