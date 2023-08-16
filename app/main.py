import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

PARAMS = {
    "key": API_KEY,
    "q": CITY
}


def get_weather() -> None:
    res = requests.get(URL, params=PARAMS)

    if res.status_code == 200:
        data = res.json()
        print(f"Performing request to Weather API for {CITY}")

        city = data.get("location")["name"]
        country = data.get("location")["country"]
        time = data.get("location")["localtime"]
        temp = data.get("current")["temp_c"]
        condition = data.get("current")["condition"]["text"]

        print(f"{city}/{country} {time} Weather: {temp} Celsius, {condition}")
    else:
        print("ERROR", res.status_code)


if __name__ == "__main__":
    get_weather()
