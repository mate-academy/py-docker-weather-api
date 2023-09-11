import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
PARAMS = {
    "key": API_KEY,
    "q": "Paris"
}


def get_weather() -> None:
    response = requests.get(url=URL, params=PARAMS)

    if response.status_code == 200:
        data = response.json()
        city = data.get("location")["name"]
        localtime = data.get("location")["localtime"]
        temp_c = data.get("current")["temp_c"]
        wind_kph = data.get("current")["wind_kph"]

        print(
            f"The weather in {city} {localtime} \n"
            f"Temperature: {temp_c}°C \n"
            f"Wind: {wind_kph} km/h \n"
        )

    else:
        print(response.status_code)


if __name__ == "__main__":
    get_weather()
