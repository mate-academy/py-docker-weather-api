import os
import requests
import sys


BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("Error: Please set API_KEY environment variable")
        sys.exit(1)

    try:
        response = requests.get(
            BASE_URL,
            params={"key": API_KEY, "q": CITY},
            timeout=10
        )
        response.raise_for_status()
        weather = response.json()

        print(f"Weather in {weather['location']['name']} right now:")
        print(f"Temperature: {weather['current']['temp_c']}°C")
        print(f"Condition: {weather['current']['condition']['text']}")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
