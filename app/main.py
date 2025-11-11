import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&"
FILTERING = "Kyiv"


def get_weather() -> None:
    result = requests.get(URL + f"q={FILTERING}&aqi=no").json()
    print(
        f"{result["location"]["name"]}/{result["location"]["country"]} "
        f"{result["location"]["localtime"]} Weather: "
        f"{result["current"]["temp_c"]} Celsius, "
        f"{result["current"]["condition"]["text"]}"
    )


if __name__ == "__main__":
    get_weather()
