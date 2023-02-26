import os

import requests
import json

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    api_key = os.environ["API_KEY"]
    request = requests.get(URL + f"q={FILTERING}" + f"&key={api_key}")

    data = json.loads(request.text)
    location = data["location"]
    weather = data["current"]

    city = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    print(f"{city}/{country} {localtime} ", end="")

    temperature = weather["temp_c"]
    description = weather["condition"]["text"]
    print(f"Weather: {temperature} Celsius, {description}")


if __name__ == "__main__":
    get_weather()
