import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    if API_KEY is None:
        raise ValueError("API_KEY environment variable not set")

    print("Performing request to Weather API for city Paris...")
    response = requests.get(
        URL,
        params={"key": API_KEY, "q": FILTERING},
    )
    data = response.json()
    data_location = data["location"]
    data_current = data["current"]
    data_condition = data_current["condition"]
    print(
        f"{data_location['name']}/{data_location['country']} "
        f"{data_location['localtime']} "
        f"Weather: {data_current['temp_c']} Celsius, {data_condition['text']}"
    )


if __name__ == "__main__":
    get_weather()
