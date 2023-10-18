import requests
import os
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json?"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    result = requests.get(URL + f"key={API_KEY}&q={CITY}")

    print(result.text)


if __name__ == "__main__":
    get_weather()
