import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
REQUEST_TIMEOUT = 10


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise RuntimeError(
            "Set the API_KEY environment variable before running."
        )

    print(f"Performing request to Weather API for {CITY} city.")
    response = requests.get(
        API_URL,
        params={"key": api_key, "q": CITY},
        timeout=REQUEST_TIMEOUT,
    )
    response.raise_for_status()
    weather = response.json()

    location = weather["location"]
    current = weather["current"]
    print(
        f"{location['name']}/{location['country']} {location['localtime']} "
        f"Weather: {current['temp_c']} Celsius, "
        f"{current['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
