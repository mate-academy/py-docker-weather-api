import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:

    result = requests.get(BASE_URL + f"key={API_KEY}" + "&" + f"q={FILTERING}")
    if result.status_code == 200:
        country = result.json()["location"]["country"]
        city = result.json()["location"]["name"]
        local_time = result.json()["location"]["localtime"]
        temperature = result.json()["current"]["temp_c"]
        condition = result.json()["current"]["condition"]["text"]
        print(
            f"{country}/{city} {local_time} "
            f"Weather: {temperature} Celsius, {condition}"
        )


if __name__ == "__main__":
    get_weather()
