import os

import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise Exception("API_KEY is not set")


def get_weather() -> None:
    url = f"{URL}key={API_KEY}&q={FILTERING}&aqi=no"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        cloud = data["current"]["cloud"]
        info_weather = (f"City: {city}, Temp: {temperature}, "
                        f"Humidity: {humidity}, Cloud: {cloud}")
        print(info_weather)
    else:
        errors = f"Bad request data: {response.status_code} != 200"
        print(errors)


if __name__ == "__main__":
    get_weather()
