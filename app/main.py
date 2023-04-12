import os
import requests
from requests import HTTPError

URL = f"https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    try:
        API_KEY = os.environ.get("API_KEY")
        response = requests.get(
            URL + f"key={API_KEY}" + f"&q={FILTERING}" + "&aqi=no"
        )
        weather_data_dict = response.json()
        location_data = weather_data_dict.get("location")
        temperature_data = weather_data_dict.get("current")
        condition_data = temperature_data.get("condition")
        result = (
            f"{location_data['name']}/{location_data['country']}"
            f" {location_data['localtime']} Weather: {temperature_data['temp_c']}"
            f" Celsius, {condition_data['text']}"
        )
        print(f"Performing request to Weather API for city {FILTERING}...")
        print(result)
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as other_err:
        print(f"Other error occurred: {other_err}")


if __name__ == "__main__":
    get_weather()
