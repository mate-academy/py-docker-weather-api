import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ["API_KEY"]


def get_weather() -> None:
    result = requests.get(URL, params={"key": API_KEY, "q": FILTERING})
    print("Performing request to Weather API for city Paris...")
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
