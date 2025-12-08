import requests
import os
import sys

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("Error: API_KEY is not set.")
    sys.exit(1)


def get_weather() -> dict:
    try:
        URL = "http://api.weatherapi.com/v1/current.json"
        FILTERING = "Paris"

        params = {"key": API_KEY, "q": FILTERING}

        result = requests.get(URL, params=params)
        result.raise_for_status()
        data = result.json()
        print(data)
        return data
    except requests.RequestException as e:
        print(f"Error fetching weather: {e}")
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}


if __name__ == "__main__":
    get_weather()
