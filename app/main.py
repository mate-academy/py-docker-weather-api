import os

import requests

WEATHER_API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
LOCATION = "Paris"


def get_weather() -> str:
    response = requests.get(f"{BASE_URL}?q={LOCATION}&key={WEATHER_API_KEY}")
    if response.status_code == 200:
        data = response.json()
        location = data.get("location", {})
        current = data.get("current", {})

        country = location.get("country")
        localtime = location.get("localtime")
        celsius = current.get("temp_c")
        condition = current.get("condition", {}).get("text")

        return (f"{LOCATION}/{country} {localtime} "
                f"Weather: {celsius} Celsius, {condition}")
    else:
        return f"Error {response.status_code}"


if __name__ == "__main__":
    print(f"Performing request to Weather API for city {LOCATION}")
    print(get_weather())
