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

    print(
        f"{location["name"]}/{location["country"]} "
        f"{location["localtime"]} Weather: "
        f"{current["temp_c"]} Celsius, "
        f"{current["condition"]["text"]}"
    )


if __name__ == "__main__":
    get_weather()
