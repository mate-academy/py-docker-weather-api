import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    params = {
        "key": api_key,
        "q": CITY,
    }

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(URL, params=params)
    response.raise_for_status()

    weather_data = response.json()

    location = weather_data["location"]
    current = weather_data["current"]

    city = location["name"]
    country = location["country"]
    local_time = location["localtime"]
    temperature = current["temp_c"]
    condition = current["condition"]["text"]

    print(
        f"{city}/{country} {local_time} Weather: "
        f"{temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
