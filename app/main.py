import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    result = requests.get(
        f"{URL}key={API_KEY}&q={FILTERING}"
    ).json()

    print(f"{result.get('location').get('name')}"
          f"/{result.get('location').get('country')}"
          f" {result.get('location').get('localtime')}"
          f" Weather: {result.get('current').get('temp_c')} Celsius, "
          f"{result.get('current').get('condition').get('text')}")


if __name__ == "__main__":
    get_weather()
