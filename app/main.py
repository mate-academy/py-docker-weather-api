import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
TIMEOUT = 10


def get_weather() -> None:
    api_key = os.environ["API_KEY"]

    response = requests.get(
        URL,
        params={"key": api_key, "q": FILTERING},
        timeout=TIMEOUT,
    )
    response.raise_for_status()

    weather = response.json()
    location = weather["location"]
    current = weather["current"]

    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
