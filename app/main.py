import os
import sys
import requests


WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("ERROR: API_KEY environment variable is not set", file=sys.stderr) # noqa501
        sys.exit(1)

    params = {
        "key": api_key,
        "q": CITY,
        "aqi": "no",
    }

    try:
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"ERROR: request failed: {e}", file=sys.stderr)
        sys.exit(1)

    location = data.get("location", {})
    current = data.get("current", {})

    print(f"City: {location.get('name')}, {location.get('country')}")
    print(f"Condition: {current.get('condition', {}).get('text')}")
    print(f"Temperature (C): {current.get('temp_c')}")
    print(f"Feels like (C): {current.get('feelslike_c')}")
    print(f"Wind (kph): {current.get('wind_kph')}")
    print(f"Humidity (%): {current.get('humidity')}")


if __name__ == "__main__":
    get_weather()
