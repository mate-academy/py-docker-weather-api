import os
import requests


API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    result = requests.get(URL + f"key={API_KEY}&q={FILTERING}").json()
    city = result["location"]["name"]
    country = result["location"]["country"]
    localtime = result["location"]["localtime"]
    condition = result["current"]["condition"]["text"]
    temp_c = result["current"]["temp_c"]
    print(f"{city}/{country} {localtime} Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
