import os
import sys
import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = os.getenv("CITY", "Paris")

    if not api_key:
        print("ERROR: API_KEY env var is not set.", file=sys.stderr)
        sys.exit(1)

    try:
        resp = requests.get(
            API_URL,
            params={"key": api_key, "q": CITY},
            timeout=10
        )
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)

    loc = data.get("location", {})
    cur = data.get("current", {})

    city = loc.get("name", CITY)
    country = loc.get("country", "")
    localtime = loc.get("localtime", "")
    temp_c = cur.get("temp_c")
    condition = (cur.get("condition") or {}).get("text", "")

    temp_str = f"{temp_c: .1f}" if isinstance(temp_c, (int, float)) else "N/A"
    print(f"{city}/{country} "
          f"{localtime} Weather: "
          f"{temp_str} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
