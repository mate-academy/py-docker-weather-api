import os
import sys
from typing import Any, Dict

import requests

# Constantes de configuração
BASE_URL = "http://api.weatherapi.com/v1"
ENDPOINT = "/current.json"
CITY = "Paris"
REQUEST_TIMEOUT = 10  # seconds

# Constantes exigidas pela checklist
API_KEY_ENV = "API_KEY"  # nome da variável de ambiente
PARAM_API_KEY = "key"  # nome do parâmetro de API key na querystring
PARAM_QUERY = "q"  # nome do parâmetro de localização na querystring


def get_api_key() -> str:
    api_key = os.getenv(API_KEY_ENV)
    if not api_key:
        raise RuntimeError(
            "Missing API_KEY environment variable. "
            "Set API_KEY with your WeatherAPI key."
        )
    return api_key


def fetch_current_weather(api_key: str) -> Dict[str, Any]:
    url = f"{BASE_URL}{ENDPOINT}"
    params = {PARAM_API_KEY: api_key, PARAM_QUERY: CITY}
    response = requests.get(url, params=params, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()


def print_paris_weather(payload: Dict[str, Any]) -> None:
    location = payload.get("location", {})
    current = payload.get("current", {})
    condition_obj = current.get("condition") or {}
    condition = condition_obj.get("text", "n/a")

    name = location.get("name", "Paris")
    country = location.get("country", "")
    temp_c = current.get("temp_c", "n/a")
    feels_c = current.get("feelslike_c", "n/a")
    humidity = current.get("humidity", "n/a")
    wind_kph = current.get("wind_kph", "n/a")

    line = (
        f"{name}, {country}: {temp_c}°C "
        f"(feels {feels_c}°C), "
        f"{condition}. Humidity {humidity}%, "
        f"wind {wind_kph} kph."
    )
    print(line)


def main() -> int:
    try:
        api_key = get_api_key()
        data = fetch_current_weather(api_key)
        print_paris_weather(data)
        return 0
    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response else "N/A"
        print(f"HTTP error: {status} {exc}", file=sys.stderr)
        return 1
    except requests.RequestException as exc:
        print(f"Network error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
