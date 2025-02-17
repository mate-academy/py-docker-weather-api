import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    response = requests.get(
        API_URL, params={"key": os.getenv("API_KEY"), "q": FILTERING}
    )
    print(response.json())


if __name__ == "__main__":
    get_weather()
