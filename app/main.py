import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.environ["API_KEY"]
    print(f"Performing request to Weather API for city {FILTERING}...")
    response = requests.get(URL, params={"key": api_key, "q": FILTERING})
    response.raise_for_status()
    data = response.json()
    location_name = data["location"]["name"]
    location_country = data["location"]["country"]
    location_localtime = data["location"]["localtime"]
    weather_temp = data["current"]["temp_c"]
    weather_condition = data["current"]["condition"]["text"]
    print(
        f"{location_name}/{location_country} "
        f"{location_localtime} Weather: {weather_temp} "
        f"Celsius, {weather_condition}"
    )


if __name__ == "__main__":
    get_weather()
