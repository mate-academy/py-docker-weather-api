import os
import sys

import requests


LOCATION = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/forecast.json"


def get_weather() -> None:
    secret_key = os.getenv("API_KEY")
    if not secret_key:
        print(
            "ERROR: API_KEY is missing in environment variables",
            file=sys.stderr
        )
        sys.exit(1)

    params = {
        "key": secret_key,
        "q": LOCATION,
        "days": 7,
        "aqi": "no",
        "alerts": "no"
    }

    print(f"Fetching weather for {LOCATION}", flush=True)

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        current_temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(
            f"SUCCESS: Weather in {LOCATION}: {current_temp}°C, {condition}",
            flush=True
        )

    except requests.exceptions.RequestException as e:
        print(f"REQUEST FAILED: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
