import os
import sys
import requests

API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = os.getenv("CITY", "Paris")
    if not api_key:
        print("ERROR: API_KEY env var is required", file=sys.stderr)
        sys.exit(1)

    try:
        resp = requests.get(
            API_URL,
            params={"key": api_key, "q": city},
            timeout=15
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"ERROR: request failed: {e}", file=sys.stderr)
        sys.exit(1)

    data = resp.json()
    loc = data.get("location", {}).get("name", city)
    cur = data.get("current", {})
    temp_c = cur.get("temp_c", "?")
    condition = (cur.get("condition") or {}).get("text", "N/A")
    humidity = cur.get("humidity", "?")
    wind_kph = cur.get("wind_kph", "?")

    try:
        temp_str = f"{float(temp_c): .1f}°C"
    except (TypeError, ValueError):
        temp_str = f"{temp_c}°C"

    print(f"{loc}: {temp_str}, "
          f"{condition}, humidity "
          f"{humidity}%, wind {wind_kph} kph")


if __name__ == "__main__":
    get_weather()
