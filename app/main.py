import os
import requests

# Згідно з рекомендаціями ментора, визначаємо API URL та місто як константи.
API_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather(api_key: str) -> None:
    """
    Gets current weather for the predefined city (Paris).
    """
    # Тепер функція не приймає місто як параметр, а використовує константу.
    params = {"key": api_key, "q": CITY}
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()

        # Оновлюємо парсинг відповіді,щоб він відповідав формату WeatherAPI.com
        if "current" in data and "temp_c" in data["current"]:
            temperature = data["current"]["temp_c"]
            print(f"Current temperature in {CITY}: {temperature}°C")
        else:
            print(f"Could not get weather data for {CITY}. Response: {data}")

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")


if __name__ == "__main__":
    # Read API key from environment variable
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY environment variable is not set.")
    else:
        # **ВИПРАВЛЕНО:** Виклик функції тепер передає тільки api_key.
        # "Paris" було видалено, оскільки воно вже є константою CITY.
        get_weather(api_key)
