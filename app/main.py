import os
import sys
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("❌ ERROR: API_KEY is not set in environment variables.",
              file=sys.stderr)
        sys.exit(1)

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"❌ Request failed: {e}", file=sys.stderr)
        sys.exit(1)

    data = response.json()
    location = data.get("location", {}).get("name", "Unknown")
    temp_c = data.get("current", {}).get("temp_c", "N/A")
    condition = data.get("current", {}).get("condition", {}).get("text", "N/A")

    print(f"📍 Weather in {location}")
    print(f"🌡️ Temperature: {temp_c}°C")
    print(f"☁️ Condition: {condition}")


if __name__ == "__main__":
    get_weather()
