import os

import requests

BASE_URL = "http://api.weatherapi.com/v1"
API_KEY = os.environ.get("API_KEY")

FILTERING_CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise Exception("API_KEY environment variable is not set")

    response = requests.get(
        url=f"{BASE_URL}/current.json",
        params={
            "key": API_KEY,
            "q": FILTERING_CITY,
        },
    )
    response.raise_for_status()

    data = response.json()

    location = data.get("location", {})
    current_weather = data.get("current", {})

    city = location.get("name", "Unknown")
    country = location.get("country", "Unknown")
    datetime = location.get("localtime", "Unknown")
    temp_c = current_weather.get("temp_c", "N/A")
    condition = current_weather.get("condition", {}).get("text", "Unknown")

    print(
        f"{city}/{country} {datetime} Weather: {temp_c}° Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
