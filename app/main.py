import os

import requests

API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather():
    parameters = {"key": API_KEY,
                  "q": CITY}
    response = requests.get(BASE_URL, parameters)
    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{city}/{country} {time} Weather: "
          f"{temperature} Celsius, {condition}")



if __name__ == "__main__":
    get_weather()
