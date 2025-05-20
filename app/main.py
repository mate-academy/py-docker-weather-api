import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:

    params = {
        "key": API_KEY,
        "q": "Paris"
    }

    response = requests.get(url=URL, params=params)
    data = response.json()
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']}"
        f" Weather: {data['current']['temp_c']} "
        f"Celsius, {data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
