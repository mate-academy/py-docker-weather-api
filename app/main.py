import os
import sys

import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
REQUEST_TIMEOUT = 10


def get_weather() -> None:
    api_key = os.environ.get("API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("Set the API_KEY environment variable.")

    print(f"Performing request to Weather API for city {CITY}...")
    try:
        response = requests.get(
            URL,
            params={"key": api_key, "q": CITY},
            timeout=REQUEST_TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException:
        # Request exceptions may include a URL containing the API key.
        raise RuntimeError("Unable to retrieve weather from Weather API.") \
            from None

    try:
        data = response.json()
        location = data["location"]
        current = data["current"]
        weather = (
            "{name}/{country} {localtime} Weather: {temperature} Celsius, "
            "{condition}"
        ).format(
            name=location["name"],
            country=location["country"],
            localtime=location["localtime"],
            temperature=current["temp_c"],
            condition=current["condition"]["text"],
        )
    except (ValueError, KeyError, TypeError):
        raise RuntimeError("Weather API returned an invalid response.") \
            from None
    print(weather)


if __name__ == "__main__":
    try:
        get_weather()
    except RuntimeError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
