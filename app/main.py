import os
import requests


URL = "https://api.weatherapi.com/v1/current.json?"
KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    result = requests.get(f"{URL}key={KEY}&q={CITY}")
    result_dict = result.json()
    country = result_dict["location"]["country"]
    city = result_dict["location"]["name"]
    time = result_dict["current"]["last_updated"]
    temp_c = result_dict["current"]["temp_c"]
    condition = result_dict["current"]["condition"]["text"]
    print("Performing request to Weather API for city Paris...")
    print(f"{city}/{country} {time} Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
