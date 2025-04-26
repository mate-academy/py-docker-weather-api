import os
import requests


BASE_URL = "https://api.weatherapi.com/v1/current.json"
DEFAULT_CITY = "Paris"


def get_weather(city: str = DEFAULT_CITY) -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise EnvironmentError("API_KEY not found in environment variables")

    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Weather in {city}: {temperature}°C, {condition}")


if __name__ == "__main__":
    get_weather()
