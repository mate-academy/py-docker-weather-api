import os
import requests

WEATHER_API_URL = "http://api.weatherapi.com/v1"
API_METHOD = "current.json"
CITY = "Paris"


def get_weather(api_key: str) -> None:
    url = f"{WEATHER_API_URL}/{API_METHOD}?key={api_key}&q={CITY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["current"]["last_updated"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(
            f"Weather in {city}, {country} (local time {local_time}): "
            f"Temperature: {temp_c}°C",
            f"Condition: {condition}"
        )
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


def get_api_key() -> str:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print(
            "Weather API key not found. "
            "Set the WEATHER_API_KEY environment variable."
        )
    return api_key


if __name__ == "__main__":
    print(f"Performing request to WeatherAPI for city {CITY}...")
    api_key = get_api_key()
    if api_key:
        get_weather(api_key)
