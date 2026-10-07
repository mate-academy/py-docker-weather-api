import os

import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    params = {"key": api_key, "q": FILTERING}
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    location = data.get("location", {})
    current = data.get("current", {})
    city = location.get("name", FILTERING)
    country = location.get("country", "France")
    localtime = location.get("localtime", "")
    temperature = current.get("temp_c", 0)
    condition = current.get("condition", {}).get("text", "Unknown")

    print(
        f"{city}/{country} {localtime} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
