import requests
import os

KEY = os.environ["API_KEY"]
URL = f"https://api.weatherapi.com/v1/current.json?key={KEY}&q=Paris"


def get_weather():
    data = requests.get(URL, KEY).json()

    date_time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]

    print(
        f"In Paris {date_time} "
        f"air temperature is {temperature} °C"
    )


if __name__ == "__main__":
    get_weather()
