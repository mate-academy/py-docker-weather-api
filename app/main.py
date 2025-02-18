import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    res = requests.get(f"{BASE_URL}?q={CITY}&key={API_KEY}")
    print("Performing request to Weather API for city Paris...")
    data = res.json()
    print(
        f"{data['location']['name']}/{data['location']['country']}"
        f" {data['location']['localtime']}"
        f" Weather: {data['current']['temp_c']} Celsius,"
        f" {data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
