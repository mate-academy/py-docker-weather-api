import logging
import os
import requests

API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = os.getenv("CITY", "Paris")


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    if not api_key:
        logging.error("API_KEY environment variable is not set")
        raise ValueError("API_KEY environment variable is required")

    params = {
        "key": api_key,
        "q": CITY,
    }

    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()

        weather_data = response.json()

        current = weather_data["current"]
        print(f"Current weather in {CITY}:")
        print(f"Temperature: {current['temp_c']}°C")
        print(f"Condition: {current['condition']['text']}")

    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
