import os
import requests
import json

from typing import Union


URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("WEATHER_API_KEY")
CITY = "Paris"


def get_weather() -> Union[dict, str]:
    response = requests.get(
        URL + f"q={CITY}&key={API_KEY}"
    ).json()

    print(
        f"Weather in {CITY}:\n"
        f"{json.dumps(response, indent=2)}"
    )


if __name__ == "__main__":
    if not API_KEY:
        raise ValueError("WEATHER_API_KEY environment variable is not set.")

    get_weather()
