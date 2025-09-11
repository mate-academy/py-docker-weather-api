import os
import requests


API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    url = f"{BASE_URL}?key={API_KEY}&q={CITY}&aqi=no"

    response = requests.get(url)
    data = response.json()

    city_name = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]

    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city_name}...")
    print(f"{city_name}/{country} {local_time} Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
