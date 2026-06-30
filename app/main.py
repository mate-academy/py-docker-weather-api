import os
import sys
import requests

CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        sys.exit(1)

    url = f"{BASE_URL}?key={api_key}&q={CITY}"

    print(f"Performing request to Weather API for city {CITY}...")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        city_name = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(
            f"{city_name}/{country} {localtime} "
            f"Weather: {temp_c} Celsius, {condition}"
        )

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
