import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY environment variable not set.")
        return
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"
    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        wind_speed = weather_data["current"]["wind_kph"]
        print(
            f"Current weather in Paris: "
            f"temperature {temperature}°C, {condition}, "
            f"wind speed: {wind_speed} km/h"
        )
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    get_weather()
