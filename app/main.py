import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ["API_KEY"]

    res = requests.get(
        URL,
        params={"key": api_key, "q": CITY},
    )

    data = res.json()

    city = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    humidity = data["current"]["humidity"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature} C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity} %")


if __name__ == "__main__":
    get_weather()
