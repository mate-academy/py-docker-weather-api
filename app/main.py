import os
import requests


API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY environment variable is required")

    url = f"{BASE_URL}?key={API_KEY}&q={CITY}&aqi=no"

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    city_name = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]

    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city_name}...")
    print(
        f"{city_name}/{country} {local_time} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
