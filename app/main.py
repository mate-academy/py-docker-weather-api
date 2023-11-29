import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY_FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    url = BASE_URL + f"?key={API_KEY}" + f"&q={CITY_FILTERING}"
    res = requests.get(url)

    if res.status_code == 200:
        weather_dict = res.json()

        location = weather_dict.get("location").get("name")
        last_updated = weather_dict.get("current").get("last_updated")
        temp_c = weather_dict.get("current").get("temp_c")
        humidity = weather_dict.get("current").get("humidity")
        condition_text = (weather_dict.get("current")
                          .get("condition")
                          .get("text"))

        print(f"Location: {location}")
        print(f"Condition: {condition_text}")
        print(f"Last updated: {last_updated}")
        print(f"Temperature: {temp_c} C")
        print(f"Humidity: {humidity} %")
    else:
        print(f"There is {res.status_code} error with your request")


if __name__ == "__main__":
    get_weather()
