import os

import requests

BASE_URL = "http://api.weatherapi.com/v1"

ENDPOINT = "/current.json"

CITY = "Paris"


def get_weather() -> None:
    req = requests.get(
        BASE_URL + ENDPOINT,
        headers={
            "Content-Type": "application/json",
            "key": os.environ.get("WEATHER_API"),
        },
        params={
            "q": CITY,
        },
    ).json()

    print(f"Performing request to Weather API for city {req["location"]["name"]}...")
    print(
        f"{req['location']['name']}/{req['location']['country']} {req['location']['localtime']} "
        f"Weather: {req['current']['temp_c']} Celsius, {req['current']['condition']["text"]}."
    )


if __name__ == "__main__":
    get_weather()
