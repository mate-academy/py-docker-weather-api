import os

import requests


def get_weather() -> None:
    api_url = "https://api.weatherapi.com/v1/current.json"
    city_name = "Paris"
    url = (f"{api_url}?key={os.environ['API_KEY']}&q={city_name}&aqi=no")
    response = requests.get(url)
    location_info = response.json()["location"]
    current_info = response.json()["current"]
    print("Performing request to Weather API for city Paris...")
    print(
        f"Paris/France {location_info['localtime']} "
        f"Weather: {current_info['temp_c']} Celsius, "
        f"{current_info['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
