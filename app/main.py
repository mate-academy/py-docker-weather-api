import os
import sys

import requests

WEATHER_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable not set.")

    city = "Paris"
    if len(sys.argv) > 1:
        city = sys.argv[1]

    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }

    print(f"Performing request to Weather API for city {city}...")
    response = requests.get(WEATHER_URL, params=params)
    response.raise_for_status()

    data = response.json()

    location_data = data["location"]
    current_data = data["current"]

    city_name = location_data["name"]
    country = location_data["country"]
    localtime = location_data["localtime"]
    temp_celsius = current_data["temp_c"]
    condition_text = current_data["condition"]["text"]

    output = (
        f"{city_name}/{country} {localtime} "
        f"Weather: {temp_celsius} Celsius, {condition_text}"
    )
    print(output)


if __name__ == "__main__":
    try:
        get_weather()
    except ValueError as e:
        print(e)
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code in (401, 403):
            print("HTTP Error: Invalid API Key.")
        elif e.response.status_code == 400:
            print("HTTP Error: City not found.")
        else:
            print(f"HTTP Error: {e}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        sys.exit(1)
