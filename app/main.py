import os

import requests

API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

REQUEST_PARAMS = {
    "key": API_KEY,
    "q": "Paris"
}


def get_weather():
    request = requests.get(BASE_URL, REQUEST_PARAMS)
    json_data = request.json()

    country = json_data["location"]["country"]
    city = json_data["location"]["name"]
    time = json_data["location"]["localtime"]
    temperature = json_data["current"]["temp_c"]
    condition = json_data["current"]["condition"]["text"]
    print(f"{city}/{country} {time}"
          f" Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
