import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> str:
    key = os.environ.get("API_KEY")
    if not key:
        raise ValueError("API_KEY not set")
    result = requests.get(
        URL,
        params={
            "key": key,
            "q": FILTERING,
        }
    )
    if result.status_code != 200:
        result.raise_for_status()
    data = result.json()
    city = data["location"].get(
        "name", "No city"
    )
    country = data["location"].get(
        "country",
        "No country"
    )
    last_update = data["current"].get(
        "last_updated",
        "No last_updated"
    )
    temp_c = data["current"].get(
        "temp_c",
        "No temperature"
    )
    condition = data["current"]["condition"].get(
        "text",
        "No condition"
    )
    return (
        f"{city}/{country} {last_update} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    print(get_weather())
