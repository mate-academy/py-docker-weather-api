import os

import requests
from dotenv import load_dotenv


load_dotenv()
URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    result = requests.get(URL + f"?q={CITY}&key={API_KEY}")
    print("Performing request to Weather API for city Paris...")
    data = result.json()
    print(
        f"{data['location']['name']}/{data['location']['country']}"
        f" {data['location']['localtime']}"
        f" Weather: {data['current']['temp_c']} Celsius,"
        f" {data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
