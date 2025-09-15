import os
from typing import Any

import requests


API_KEY = os.environ.get("API_KEY")
FILTERING = "Paris"
URL = "http://api.weatherapi.com/v1/current.json?key="


def validate(parameter: Any) -> None:
    if parameter is None:
        raise ValueError("Requested data was not found in the response")


def get_weather() -> None:
    response = requests.get(URL + f"{API_KEY}&q={FILTERING}")
    data = response.json()
    current = data.get("current")
    validate(current)
    temperature = current.get("temp_c")
    validate(temperature)
    last_updated = current.get("last_updated")
    validate(last_updated)
    condition = current.get("condition")
    validate(condition)
    condition_text = condition.get("text")
    validate(condition_text)
    print(f"Paris/France {last_updated} "
          f"Weather: {temperature} Celsius, {condition_text}")


if __name__ == "__main__":
    get_weather()
