import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": CITY,
        }
    ).json()
    print(
        f"Performing request to Weather API for city {CITY}...\n"
        f"{response['location']['name']}/{response['location']['country']} "
        f"{response['current']['last_updated']} Weather: "
        f"{response['current']['temp_c']} Celsius "
        f"{response['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
