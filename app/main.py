import os

import requests


URL = "http://api.weatherapi.com/v1/current.json"

PARAMS = {
    "q": "Paris",
    "key": os.environ.get("API_KEY")
}


def get_weather() -> None:
    result = requests.get(url=URL, params=PARAMS)
    location = result.json()["location"]
    current_weather = result.json()["current"]

    city = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    temperature_celsius = current_weather["temp_c"]
    weather_condition = current_weather["condition"]["text"]

    output = (f"{city}/{country} {localtime} "
              + f"Weather: {temperature_celsius} Celsius, "
              + f"{weather_condition}")
    print(output)


if __name__ == "__main__":
    get_weather()
