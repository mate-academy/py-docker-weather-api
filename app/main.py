import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        return

    params = {
        "key": api_key,
        "q": CITY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()

        weather_data = response.json()

        location = weather_data["location"]["name"]
        condition = weather_data["current"]["condition"]["text"]
        temp_c = weather_data["current"]["temp_c"]

        print(f"Current weather in {location}: {condition}, {temp_c}°C")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
