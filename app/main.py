import os

import requests


API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("API KEY not found. Set environment variable.")
        return
    params = {
        "key": API_KEY,
        "q": FILTERING
    }
    print(f"Performing request to Weather API for city {FILTERING}...")

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error while getting weather data:", e)
        return

    data = response.json()
    location = data.get("location", {})
    current = data.get("current", {})
    city = location.get("name", "N/A")
    country = location.get("country", "N/A")
    time = current.get("last_updated", "N/A")
    temp = current.get("temp_c", "N/A")
    condition = current.get("condition", {})
    condition_text = condition.get("text", "N/A")
    print(f"{city}/{country} {time} Weather: {temp} Celsius, {condition_text}")


if __name__ == "__main__":
    get_weather()
