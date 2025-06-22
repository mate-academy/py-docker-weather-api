import os
from typing import Dict, Optional, Any

import requests

BASE_URL = "http://api.weatherapi.com/v1"
API_KEY = os.environ.get("API_KEY")

FILTERING_CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise Exception("API_KEY environment variable is not set")

    data = do_request(base_url=BASE_URL, api_key=API_KEY, city=FILTERING_CITY)

    location = data.get("location", {})
    current_weather = data.get("current", {})

    city = location.get("name", "Unknown")
    country = location.get("country", "Unknown")
    datetime = location.get("localtime", "Unknown")
    temp_c = current_weather.get("temp_c", "N/A")
    condition = current_weather.get("condition", {}).get("text", "Unknown")

    print(
        f"{city}/{country} {datetime} Weather: {temp_c}° Celsius, {condition}"
    )


def do_request(
    base_url: str = BASE_URL,
    api_key: str = API_KEY,
    city: str = FILTERING_CITY,
) -> Optional[Dict[str, Any]]:
    try:
        response = requests.get(
            url=f"{BASE_URL}/current.json",
            params={
                "key": API_KEY,
                "q": FILTERING_CITY,
            },
        )
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")

    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    else:
        return data


if __name__ == "__main__":
    get_weather()
