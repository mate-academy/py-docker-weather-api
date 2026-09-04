import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
DEFAULT_LOCATION = "Paris"


def get_weather(location: str = DEFAULT_LOCATION) -> None:
    api_key = os.getenv("API_KEY")

    if api_key is None:
        raise RuntimeError("API_KEY environment variable is not set")

    url = f"{URL}?key={api_key}&q={location}&aqi=no"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print(response.json())


if __name__ == "__main__":
    get_weather()
