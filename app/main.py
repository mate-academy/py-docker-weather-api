import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:

    try:
        response = requests.get(URL + f"?key={API_KEY}&q={FILTERING}")
        response.raise_for_status()
        data = response.json()

        country = data.get("location").get("country")
        localtime = data.get("location").get("localtime")
        temperature = data.get("current").get("temp_c")
        condition = data.get("current").get("condition").get("text")

        print(f"Performing requests to Weather API for city {FILTERING}...")
        print(f"{FILTERING}/{country} {localtime} "
              f"Weather: {temperature} Celsius, {condition}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()