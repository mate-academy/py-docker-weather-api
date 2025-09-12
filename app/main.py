import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY_ENV = "API_KEY"
DEFAULT_CITY = "Paris"
PARAM_KEY = "key"
PARAM_Q = "q"

API_KEY = os.getenv(API_KEY_ENV)
if not API_KEY:
    raise ValueError(f"{API_KEY_ENV} is not set")


def get_weather() -> None:
    params = {
        PARAM_KEY: API_KEY,
        PARAM_Q: DEFAULT_CITY
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()

        current = data.get("current")
        if current and "temp_c" in current and "condition" in current:
            temp_c = current["temp_c"]
            condition = current["condition"].get("text", "No description")
            print(f"Weather in {DEFAULT_CITY}: {temp_c}°C, {condition}")
        else:
            print("Unexpected API response:", data)

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)


if __name__ == "__main__":
    get_weather()
