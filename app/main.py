import os
from dotenv import load_dotenv

import requests

load_dotenv()

CITY = "Paris"
API_KEY = os.getenv("API_KEY")
URL = (f"http://api.weatherapi.com/v1/current.json"
       f"?key={API_KEY}&q={CITY}")


def get_weather() -> None:
    response = requests.get(URL)

    if response.status_code == 200:
        print("Perfoming request to Weather API for city Paris....")
        weather_data = response.json()
        location = weather_data["location"]["name"]
        country = weather_data["location"]["country"]
        localtime = weather_data["location"]["localtime"]
        condition = weather_data["current"]["condition"]["text"]
        temperature = weather_data["current"]["temp_c"]

        print(
            f"{location}/{country} datetime: {localtime}, "
            f"Weather: {temperature} Celsius, {condition}"
        )
    else:
        print("Error. SORRY....")
        print("Response content:", response.content)


if __name__ == "__main__":
    get_weather()
