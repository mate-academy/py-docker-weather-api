import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    data = requests.get(URL + "?" + f"key={KEY}" + "&" + f"q={CITY}").json()
    location = f"{data['location']['name']}/{data['location']['country']}"
    time = f"{data['location']['localtime']}"
    weather = f"Weather: {data['current']['temp_c']} " \
              f"Celsius, {data['current']['condition']['text']}"
    print(f"{location} {time} {weather}")


if __name__ == "__main__":
    get_weather()
