# app/main.py
import os
import requests

WEATHER_API_URL = "https://api.weatherapi.com/v1/current.json"


def get_weather(city: str) -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY environment variable not set")

    url = f"{WEATHER_API_URL}?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"The weather in {location}: {temp_c}°C, {condition}")
    else:
        print(f"Failed to get weather data: "
              f"{response.status_code}, "
              f"{response.text},"
              f"{city}")


if __name__ == "__main__":
    get_weather("Paris")
