import os
import sys
import json
from typing import Any, Dict

import requests


WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def fatal(msg: str, code: int = 1) -> None:
    print(msg, file=sys.stderr)
    sys.exit(code)


def fetch_current_weather(api_key: str, city: str) -> Dict[str, Any]:
    params = {
        "key": api_key,
        "q": city,
        "aqi": "no",
    }
    try:
        resp = requests.get(WEATHER_API_URL, params=params, timeout=15)
    except requests.RequestException as e:
        fatal(f"[error] network error: {e}")

    if resp.status_code != 200:
        # Спробуємо показати тіло помилки, якщо воно є
        body = None
        try:
            body = resp.json()
        except Exception:
            body = resp.text
        fatal(f"[error] API responded with {resp.status_code}: {body}")

    try:
        data = resp.json()
    except ValueError:
        fatal("[error] invalid JSON in API response")

    # Проста перевірка на помилку від WeatherAPI
    if isinstance(data, dict) and "error" in data:
        err = data["error"]
        fatal(f"[error] API error: code={err.get('code')} "
              f"message={err.get('message')}")

    return data


def format_output(data: Dict[str, Any]) -> str:
    location = data.get("location", {})
    current = data.get("current", {})
    condition = (current.get("condition") or {}).get("text")

    out = {
        "city": location.get("name"),
        "country": location.get("country"),
        "localtime": location.get("localtime"),
        "temp_c": current.get("temp_c"),
        "feelslike_c": current.get("feelslike_c"),
        "condition": condition,
        "wind_kph": current.get("wind_kph"),
        "humidity": current.get("humidity"),
        "last_updated": current.get("last_updated"),
    }
    # Друкуємо в одному рядку JSON — зручно для автоперевірок
    return json.dumps(out, ensure_ascii=False)


def main() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        fatal("[error] API_KEY environment variable is required")

    data = fetch_current_weather(api_key, CITY)
    print(format_output(data))


if __name__ == "__main__":
    main()
