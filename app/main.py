import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY is missing. Please set it as an environment variable.")
        return

    url = f"{BASE_URL}?q={CITY}&key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Weather in {CITY}: {temp}°C, {condition}")
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
