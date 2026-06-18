# COMMAND=docker pull rer8/weather:latest

import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        print("Error: API_KEY environment variable is missing!")
        return

    try:
        response = requests.get(
            URL,
            params={
                "key": API_KEY,
                "q": FILTERING
            }
        )
        response.raise_for_status()

        data = response.json()
        city = data["location"]["name"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in {city}: {temp}°C, {condition}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
