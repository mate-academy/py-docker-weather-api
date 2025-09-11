import os
import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather(CITY: str) -> dict:
    if not API_KEY:
        raise ValueError("API key not found")
    BASE_URL = (f"http://api.weatherapi.com/v1/current.json?key="
           f"{API_KEY}&q={CITY}")
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    CITY = "Paris"
    data = get_weather(CITY)
    current = data["current"]
    print(f"Weather in {CITY}: "
          f"{current['temp_c']}°C, {current['condition']['text']}")
