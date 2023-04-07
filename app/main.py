import os

import requests as requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(
        url=URL,
        params={"key": API_KEY, "q": "Paris"}
    )

    if response.status_code != 200:
        print("Error request")

    else:

        json_data = response.json()
        temperature = json_data["current"]["temp_c"]
        wind_speed = json_data["current"]["wind_kph"]
        pressure = json_data["current"]["pressure_in"]
        localtime = json_data["location"]["localtime"]
        location = json_data["location"]["name"]

        print(f"{location} {localtime}:"
              f"Temperature {temperature},"
              f"Wind speed {wind_speed},"
              f"Pressure {pressure}")


if __name__ == "__main__":
    get_weather()
