import os

import requests
import json

URL = "http://api.weatherapi.com/v1/current.json?"


def get_weather(query_params: dict) -> None:
    query_params["key"] = os.environ["API_KEY"]
    params = "&".join([f"{k}={v}" for k, v in query_params.items()])

    print("Performing request to Weather API...")
    request = requests.get(URL + params)

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
    get_weather({"q": "Paris"})
