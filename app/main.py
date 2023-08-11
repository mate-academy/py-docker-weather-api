import datetime
import os

import requests
import json


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    print("Performing request to Weather API for city of Paris")
    api_key = os.environ.get("API_KEY")
    json_from_api = requests.request(
        method="GET",
        url=URL,
        params={"key": api_key, "q": CITY},
    )
    if json_from_api.status_code == 200:
        data = json.loads(json_from_api.content)
        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(
            f"Paris/France {date_time} "
            f"Weather: {temperature} Celsius {condition}"
        )


if __name__ == "__main__":
    get_weather()
