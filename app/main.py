import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ["API_KEY"]
CITY = "Paris"
FILTERING = {"key": API_KEY, "q": CITY}


def get_weather() -> None:
    result = requests.get(URL, params=FILTERING)
    print(f"Performing request to Weather API for city {CITY}...")
    result_json = result.json()
    location = result_json["location"]
    current = result_json["current"]
    condition = current["condition"]
    print(
        f"{location['name']}/{location['country']} {location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, {condition['text']}"
    )


if __name__ == "__main__":
    get_weather()
