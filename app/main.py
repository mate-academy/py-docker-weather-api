import os

import requests


BASE_URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ["API_KEY"]
CITY = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}
    response = requests.get(BASE_URL, params).json()

    print(
        f"Performing request to Weather API for city {CITY}...\n"
        f"{CITY}/{response['location']['country']} "
        f"{response['location']['localtime']} "
        f"Weather: {response['current']['temp_c']} Celsius, "
        f"{response['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
