import json
import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_str_for_print(response_data: dict) -> str:
    location = response_data.get("location")
    country = location.get("country")
    city = location.get("name")

    current_info = response_data.get("current")
    date = current_info.get("last_updated")
    temp_c = current_info.get("temp_c")
    condition = current_info.get("condition").get("text")

    return f"{city}/{country} {date} Weather: {temp_c} Celsius, {condition}"


def get_weather() -> None:
    payload = {
        "q": FILTERING,
        "key": API_KEY
    }

    print(f"Performing request to Weather API for city {FILTERING}...")
    response = requests.get(URL, params=payload)
    response_data = json.loads(response.content)

    if response.status_code == 200:
        print(get_str_for_print(response_data))
    else:
        print(
            f"Status code is {response.status_code}. "
            f"Error: {response_data.get('error')}"
        )


if __name__ == "__main__":
    get_weather()
