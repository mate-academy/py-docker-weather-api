import os
import requests

from dotenv import load_dotenv

load_dotenv()

CITY = "Paris"
KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"
PARAMS = {"key": KEY, "q": CITY}


def get_weather() -> None:
    result = requests.get(URL, params=PARAMS)
    if result.status_code == 200:
        data = result.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        info = data["current"]["condition"]["text"]

        print(
            f"{city}/{country} {localtime} Weather: "
            f"{temperature} Celsius, {info}"
        )
    else:
        print("Sorry, an error occured")


if __name__ == "__main__":
    get_weather()
