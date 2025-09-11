import os

import requests
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    res = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris"
    ).json()

    print(
        f"City: {res["location"]["name"]}\n"
        f"Weather: {res["current"]["condition"]["text"]}\n"
        f"Temperature: {res["current"]["temp_c"]}\n"
        f"Feels like {res["current"]["feelslike_c"]}\n"
        f"Wind: {res["current"]["wind_kph"]}\n"
        f"Clouds: {res["current"]["cloud"]}\n"
        f"Heat index: {res["current"]["heatindex_f"]}"
    )


if __name__ == "__main__":
    get_weather()
