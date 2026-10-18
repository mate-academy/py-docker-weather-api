import os

import requests

CURRENT_WEATHER_URL = "https://api.weatherapi.com/v1/current.json"

def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if api_key is None:
        raise Exception("API_KEY not set")
    print("Performing request to Weather API for city Paris...")
    query_params = {
        "key": api_key,
        "q": "Paris",
    }
    response = requests.get(CURRENT_WEATHER_URL, params=query_params)
    assert response.status_code == 200
    data = response.json()
    last_updated = data["current"]["last_updated"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(
        f"Paris/France {last_updated} Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
