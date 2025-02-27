import os
import requests


API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json?"
CITY = os.getenv("CITY", "Paris")


def get_weather(api_key: str, city: str) -> None:
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city,
        "aqi": "no"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        condition = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        time = data["location"]["localtime"]
        print(
            f"Weather in {city}: {condition}, "
            f"{temp_c}°C (Local Time: {time})"
        )
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    if not API_KEY:
        print("API_KEY environment variable is required.")
    else:
        get_weather(API_KEY, CITY)
