import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"

def get_weather() -> None:
    print("Performing request to Weather API for city Paris...")
    response = requests.get(URL, params={"key": API_KEY, "q": "Paris"})
    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{city}/{country} {localtime} Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
