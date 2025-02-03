import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTERING}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    print(
        f"{data['location']['name']}: {data['location']['country']}\n"
        f"Local Time: {data['location']['localtime']}"
        f" temp: {data['current']['temp_c']} C\n"
        f"Wind speed: {data['current']['wind_kph']} km/h"
    )


if __name__ == "__main__":
    get_weather()
