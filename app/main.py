import os
from dotenv import load_dotenv
import requests

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"
PARAMS = {
    "key": API_KEY,
    "q": CITY,
}


def get_weather() -> None:
    request = requests.get(url=URL, params=PARAMS).json()

    city = request.get("location")["name"]
    country = request.get("location")["country"]
    localtime = request.get("location")["localtime"]
    temp = request.get("current")["temp_c"]
    condition = request.get("current")["condition"]["text"]

    weather_string = (
        f"{city}/{country} {localtime} "
        f"Weather: {temp} Celsius, {condition}"
    )

    print(weather_string)


if __name__ == "__main__":
    get_weather()
