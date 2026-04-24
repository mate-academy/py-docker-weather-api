import datetime
import os
import requests


API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY
    }
    data = requests.get(URL, params=params).json()
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M")

    print(f"{country} {date} {time} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
