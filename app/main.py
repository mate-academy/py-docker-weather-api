import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set.")

    url = "https://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris",
        "aqi": "no"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Error fetching weather data: {response.json()}")

    weather_data = response.json()

    print("Current Weather in Paris:")
    print(f"Temperature: {weather_data['current']['temp_c']}°C")
    print(f"Weather: {weather_data['current']['condition']['text']}")
    print(f"Humidity: {weather_data['current']['humidity']}%")
    print(f"Wind Speed: {weather_data['current']['wind_kph']} kph")


if __name__ == "__main__":
    get_weather()
