import os
import sys
import requests


def get_weather():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        sys.exit(1)

    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        location = data["location"]["name"]
        condition = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]

        print(f"Current weather in {location}: {condition}, Temperature: {temp_c}°C")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
