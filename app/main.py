import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


PARAMETERS = {
    "key": API_KEY,
    "q": CITY,
}


def get_weather() -> None:

    response = requests.get(URL, params=PARAMETERS)

    if response.status_code == 200:
        data = response.json()

        print(f"Performing request to Weather API for city {CITY}")

        location = data.get("location")
        current = data.get("current")

        if location and current:
            city = location["name"]
            country = location["country"]
            localtime = location["localtime"]
            temperature = current["temp_c"]
            condition = current["condition"]["text"]

            print(f"{city}/{country} {localtime} "
                  f"Weather: {temperature}, {condition}")
        else:
            print(f"ERROR: {response.status_code}")


if __name__ == "__main__":
    get_weather()
