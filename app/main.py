import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ["API_KEY"]
URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"

def get_weather() -> dict:
    # write your code here
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": CITY,
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(get_weather())
