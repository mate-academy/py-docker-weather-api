import os
import requests


CITY = "Paris"
KEY = os.environ["API_KEY"]
BASE_URL = "https://api.weatherapi.com/v1/current.json"

params = {
    "q": CITY,
    "key": KEY
}


def get_weather() -> None:
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data_value = response.json()
        country = data_value["location"]["country"]
        last_data = data_value["current"]["last_updated"]
        temperature = data_value["current"]["temp_c"]
        weather = data_value["current"]["condition"]["text"]
        result_string = (f"{CITY}/{country} {last_data} "
                         f"Weather: {temperature} Celsius, {weather}")
        print(f"Performing request to Weather API for city {CITY}...")
        print(result_string)
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    get_weather()
