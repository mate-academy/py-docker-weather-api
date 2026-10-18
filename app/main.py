import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    api_key = os.environ.get("API_KEY")
    response = requests.get(
        URL,
        params={"key": api_key, "q": CITY},
        timeout=10
    )
    response.raise_for_status()
    result = response.json()
    location = result["location"]
    current = result["current"]

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
