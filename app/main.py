import os
import requests
from dotenv import load_dotenv

BASE_URL = "http://api.weatherapi.com/v1"
CURRENT_ENDPOINT = "/current.json"
DEFAULT_CITY = "Paris"

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather(city: str) -> dict:
    if not API_KEY:
        raise ValueError("API key not found")
    url = f"{BASE_URL}{CURRENT_ENDPOINT}"
    params = {"key": API_KEY, "q": city}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    CITY = "Paris"
    data = get_weather(CITY)
    current = data["current"]
    print(f"Weather in {CITY}: "
          f"{current['temp_c']}°C, {current['condition']['text']}")
