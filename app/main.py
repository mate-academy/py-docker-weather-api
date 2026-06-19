import os
import sys
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is missing.")
        sys.exit(1)

    url = f"{BASE_URL}?key={api_key}&q={CITY}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Weather in Paris: {condition}, temperature: {temp}°C")

    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
