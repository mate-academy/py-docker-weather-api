import os
import sys
import requests

API_BASE = "https://api.weatherapi.com/v1/current.json"
CITY = "Poznan"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY is not set in environment variables", file=sys.stderr)
        sys.exit(2)

    try:
        resp = requests.get(
            API_BASE,
            params={"key": api_key, "q": CITY, "aqi": "no"},
            timeout=10
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Request failed: {e}", file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Weather in {CITY}: {condition}, {temp_c}°C")


if __name__ == "__main__":
    get_weather()
