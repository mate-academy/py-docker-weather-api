import os
import requests
from dotenv import load_dotenv


API_KEY = os.getenv("API_KEY")
if not API_KEY:
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY not found in environment variables")

    response = requests.get(BASE_URL, params={"key": API_KEY, "q": CITY})
    response.raise_for_status()
    data = response.json()

    current = data["current"]
    print(f"Weather in {CITY}: ")
    print(f"Temperature: {current['temp_c']}°C")
    print(f"Condition: {current['condition']['text']}")


if __name__ == "__main__":
    get_weather()
