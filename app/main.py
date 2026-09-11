import os
import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY environment variable is missing.")

    print(f"Performing request to Weather API for city {CITY}...")

    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    location = f"{data['location']['name']}/{data['location']['country']}"
    time = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{location} {time} Weather: {temp} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
