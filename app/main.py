import json
import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    payload = {
        "key": os.getenv("API_KEY"),
        "q": CITY,
        "aqi": "no"
    }

    response = requests.get(URL, params=payload)

    res_json = json.loads(response.content)

    city = res_json["location"]["name"]
    country = res_json["location"]["country"]
    date = res_json["current"]["last_updated"]
    temp = res_json["current"]["temp_c"]
    sky = res_json["current"]["condition"]["text"]

    print(f"{city}/{country} {date} Weather: {temp} Celsius, {sky}")


if __name__ == "__main__":
    get_weather()
