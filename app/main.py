import os
import sys

import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set."
              " Please run with -e API_KEY=...")
        sys.exit(1)
    else:
        try:
            response = requests.get(
                URL,
                params={"key": api_key,
                        "q": CITY}
            )
            response.raise_for_status()
            data = response.json()
            print(
                f"Location: {data['location']['name']},"
                f" {data['location']['country']}"
            )
            print(f"Temperature: {data['current']['temp_c']}")
        except requests.exceptions.RequestException as e:
            print(f"Error: Failed to fetch weather data: {e}")
            sys.exit(1)


if __name__ == "__main__":
    get_weather()
