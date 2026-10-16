import os

import requests


API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
REQUEST_TIMEOUT = 10


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise RuntimeError("API_KEY environment variable is not set")

    print(f"Performing request to Weather API for {CITY}")

    try:
        response = requests.get(
            API_URL,
            params={
                "key": api_key,
                "q": CITY,
            },
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException:
        raise RuntimeError("Weather API request failed") from None

    weather_data = response.json()
    location = weather_data["location"]
    current_weather = weather_data["current"]

    print(
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} Weather: "
        f"{current_weather['temp_c']} Celsius, "
        f"{current_weather['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
