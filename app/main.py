import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY, "q": "Paris"})
    data = response.json()

    if response.status_code == 200:
        date = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Paris/France {date} "
              f"Weather: {temperature} Celsius, {condition}")

    else:
        errors = data["error"]["message"]
        print("Something went wrong..." + "\n" + errors)


if __name__ == "__main__":
    get_weather()
