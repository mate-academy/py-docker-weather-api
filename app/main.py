import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(
        url=URL,
        params={"key": API_KEY, "q": "Paris"}
    )
    response_json = response.json()

    if response.status_code != 200:
        print("something went wrong ")

    else:
        current_temperature = response_json["current"]["temp_c"]
        current_pressure = response_json["current"]["pressure_mb"]
        current_humidity = response_json["current"]["humidity"]

        print(f"Temperature (in celsius) = {current_temperature} "
              f"\nAtmospheric pressure (in millibars) = {current_pressure} "
              f"\nHumidity (in percentage) = {current_humidity}")


if __name__ == "__main__":
    get_weather()
