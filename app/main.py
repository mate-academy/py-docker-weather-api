import os

import requests


API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
FILTERING_CITY = "Paris"


def get_weather() -> None:
    parameters = {"key": API_KEY, "q": FILTERING_CITY}
    result = requests.get(BASE_URL, params=parameters)
    if result.status_code == 200:
        data = result.json()

        location = data["location"]
        country = location["country"]
        local_date = location["localtime"]

        current = data["current"]
        temperature_c = current["temp_c"]
        condition_t = current["condition"]["text"]

        print(f"{FILTERING_CITY}/{country} {local_date} "
              f"Weather: {temperature_c} Celsius, {condition_t}")
    else:
        print("Oops! An error occurred while receiving data. "
              f"Status code: {result.status_code}. Maybe next time...")


if __name__ == "__main__":
    get_weather()
