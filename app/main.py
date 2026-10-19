import os
import sys
import requests


CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("ERROR: API_KEY is not set")
        sys.exit(1)

    params = {
        "q": CITY,
        "key": api_key,
        "aqi": "no"
    }

    try:
        response = requests.get(URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        # Структура ответа WeatherAPI отличается от OpenWeatherMap
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        print(f"Weather in {CITY}: ")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {condition}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind} kph")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
