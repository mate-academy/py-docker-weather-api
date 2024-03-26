import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY_NAME = "Paris"
LANGUAGE = "en"


def get_weather() -> None:
    response = requests.get(
        BASE_URL,
        params={
            "key": API_KEY,
            "q": CITY_NAME,
            "lang": LANGUAGE,
            "units": "metric",
        }
    )
    if response.status_code == 200:
        data = response.json()
        country = data["location"]["country"]
        city = data["location"]["name"]
        localtime = data["location"]["localtime"]
        condition = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        feels_like_c = data["current"]["feelslike_c"]
        temp_f = data["current"]["temp_f"]
        feels_like_f = data["current"]["feelslike_f"]

        print(
            "\nCurrent weather:\n"
            f"Country: {country}\n"
            f"City: {city}\n"
            f"Localtime: {localtime}\n"
            f"Condition: {condition}\n"
            f"Temperature °C: {temp_c}, feels like {feels_like_c}\n"
            f"Temperature °F: {temp_f}, feels like {feels_like_f}\n"
        )
    else:
        raise ValueError(
            "Something went wrong :c, Please try again with valid data!"
        )


if __name__ == "__main__":
    get_weather()
