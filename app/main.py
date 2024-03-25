import os

import requests

FILTERING = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY", None)


def get_weather() -> None:
    response = requests.get(URL + f"?q={FILTERING}&key={API_KEY}").json()
    location = response["location"].get("name") + "/" + response["location"].get("country")
    localtime = response["location"].get("localtime")
    temperature = response["current"].get("temp_c")
    condition = response["current"]["condition"].get("text")
    print(
        f"{location} {localtime} Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
