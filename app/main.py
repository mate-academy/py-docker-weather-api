import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

PARAMS = {
    "key": API_KEY,
    "q": CITY,
}


def get_weather() -> None:
    response = requests.get(URL, params=PARAMS)

    if response.status_code != 200:
        print("Something went wrong, check your data input.")
        quit()

    response = response.json()
    region = response["location"]["region"]

    current_weather = response["current"]
    sun_condition = current_weather["condition"]["text"].lower()
    temp_c = current_weather["temp_c"]
    temp_f = current_weather["temp_f"]
    last_updated = current_weather["last_updated"]
    wind_speed = current_weather["wind_kph"]

    print(f"According to the latest data(last update: {last_updated}) "
          f"the weather in {CITY}, {region}, is {sun_condition}, "
          f"with the temperature of {temp_c}°C/{temp_f}°F. "
          f"Wind speed is {wind_speed}km/h.")


if __name__ == "__main__":
    get_weather()
