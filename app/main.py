import requests
import os

from dotenv import load_dotenv

load_dotenv()

URL = " https://api.weatherapi.com/v1/current.json"

PARAMS = {
    "key": os.getenv("API_KEY"),
    "q": "Paris"
}


def get_weather() -> None:
    req = requests.get(url=URL, params=PARAMS)
    weather_json = req.json()
    location = weather_json["location"]
    current_weather = weather_json["current"]
    current_condition = weather_json["current"]["condition"]["text"]
    print("Performing request to Weather API for city Paris")
    print(
        f"{location['name']}/{location['country']} {location['localtime']} "
        f"Weather: {current_weather['temp_c']}, {current_condition}"
    )


if __name__ == "__main__":
    get_weather()
