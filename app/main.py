import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    result = requests.get(URL, params={"key": API_KEY, "q": CITY}).json()

    print(
        f"{result['location']['name']}/{result['location']['country']} "
        f"{result['current']['last_updated']} "
        f"Weather: {result['current']['temp_c']} Celsius, "
        f"{result['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
