import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set")
        return

    try:
        response = requests.get(BASE_URL, params={"key": api_key, "q": CITY})
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        last_updated = data["current"]["last_updated"]

        print(f"Current weather in {location}, {country}:")
        print(f"Condition: {condition}")
        print(f"Temperature: {temp_c}°C")
        print(f"Last updated: {last_updated}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
