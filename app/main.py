import datetime
import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    print("Performing request to Weather API for city of Paris")
    request = requests.request(
        method="GET",
        url=URL,
        params={"key": API_KEY, "q": CITY},
    )

    data = request.json()
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        f"Paris/France {date_time} "
        f"Weather: {temperature} Celsius {condition}"
    )


if __name__ == "__main__":
    get_weather()
