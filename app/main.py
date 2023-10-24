import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")

PARAMS = {
    "key": API_KEY,
    "q": "Paris"
}


def get_weather() -> None:
    res = requests.get(url=API_URL, params=PARAMS)

    res.raise_for_status()

    location = res.json()["location"]
    weather = res.json()["current"]

    location_name = f"{location['name']}/{location['country']}"
    location_time = location["localtime"]
    temperature = weather["temp_c"]
    condition = weather["condition"]["text"]

    print(
        f"{location_name} {location_time} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
