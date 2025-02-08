import os
from dotenv import load_dotenv
import requests

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
        f"{data['location']['name']}: {data['location']['country']}\n \
            Local time: {data['location']['localtime']}\n \
                Temperature: {data['current']['temp_c']} Celsium\n \
                    Wind speed: {data['current']['wind_kph']} km / h"
    )


if __name__ == "__main__":
    get_weather()
