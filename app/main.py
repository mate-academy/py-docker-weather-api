import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(city: str) -> dict:
    if not API_KEY:
        raise ValueError("API key not found")
    url = (f"http://api.weatherapi.com/v1/current.json?key="
           f"{API_KEY}&q={city}")
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    city = "Paris"
    data = get_weather(city)
    current = data["current"]
    print(f"Weather in {city}: "
          f"{current['temp_c']}°C, {current['condition']['text']}")
