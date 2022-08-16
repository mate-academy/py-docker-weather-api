import os

import requests

API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather():
    url = "http://api.weatherapi.com/v1/current.json"
    req_parameters = {"key": API_KEY, "q": CITY}
    res = requests.get(url, req_parameters)

    city = res.json()["location"]["name"]
    country = res.json()["location"]["country"]
    date = res.json()["location"]["localtime"]
    temperature = res.json()["current"]["temp_c"]
    condition = res.json()["current"]["condition"]["text"]

    print(
        f"{city}/{country} {date} Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
