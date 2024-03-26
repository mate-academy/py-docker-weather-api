import os
import requests

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/"
CITY = "Paris"


def get_weather(api_key: str) -> dict:
    url = BASE_URL + f"current.json?key={api_key}&q={CITY}"
    response = requests.get(url)
    data = response.json()
    return data["current"]


def print_weather(weather: dict) -> None:
    print("Weather in Paris:")
    print(f"Temperature: {weather['temp_c']}°C")
    print(f"Condition: {weather['condition']['text']}")
    print(f"Wind: {weather['wind_kph']} km/h")


if __name__ == "__main__":
    api_key = API_KEY
    if not api_key:
        print(
            "Error: Weather API key is missing. "
            "Set WEATHER_API_KEY environment variable."
        )
    else:
        weather = get_weather(api_key)
        print_weather(weather)
