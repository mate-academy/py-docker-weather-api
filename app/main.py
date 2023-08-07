import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    weather_api_params = {"q": "Paris"}
    weather_api_params["key"] = os.getenv("API_KEY")
    weather_api_response = requests.get(
        url="https://api.weatherapi.com/v1/current.json",
        params=weather_api_params
    )
    paris_weather_json = weather_api_response.json()
    location = paris_weather_json["location"]
    current_weather = paris_weather_json["current"]
    current_condition = paris_weather_json["current"]["condition"]["text"]
    print(f"Performing request to Weather API for city Paris")
    print(
        f"{location['name']}/{location['country']} {location['localtime']} "
        f"Weather: {current_weather['temp_c']}, {current_condition}"
    )


if __name__ == "__main__":
    get_weather()
