import os

import requests

from dotenv import load_dotenv

load_dotenv()


REQUEST_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        REQUEST_URL,
        params={"key": API_KEY, "q": "Paris"}).json()

    city = response.get("location").get("name")
    country = response.get("location").get("country")
    localtime = response.get("location").get("localtime")
    temperature = response.get("current").get("temp_c")
    condition = response.get("current").get("condition").get("text")

    print(f"{city}/{country} {localtime} "
          f"Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
