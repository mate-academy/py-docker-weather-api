import os
import requests
from typing import Any, Dict

LOCATION = "Paris"
BASE_URL = "https://api.weatherapi.com/v1/current.json"


def get_api_key() -> str:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise RuntimeError("API_KEY not set. Set it as"
                           " environment variable before running.")
    return api_key


def fetch_weather(api_key: str, location: str = LOCATION) -> Dict[str, Any]:
    params = {"key": api_key, "q": location, "aqi": "no"}
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(f"Error while requesting WeatherAPI:"
                           f" {exc}") from exc
    return resp.json()


def parse_and_print(data: Dict[str, Any]) -> None:
    current = data.get("current", {})
    location = data.get("location", {})
    temp = current.get("temp_c")
    cond = current.get("condition", {}).get("text")
    localtime = location.get("localtime")
    print(f"{LOCATION} {localtime} — {temp}°C, {cond}")


def get_weather() -> None:
    api_key = get_api_key()
    data = fetch_weather(api_key)
    parse_and_print(data)


if __name__ == "__main__":
    get_weather()
