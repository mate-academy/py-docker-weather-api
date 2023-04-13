import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:

    payload = {"key": API_KEY, "q": FILTERING}
    response = requests.get(URL, params=payload)
    location = response.json()["location"]
    print(f"Performing weather for city ...{location['region']}")
    data = response.json()["current"]
    weather = f"{location['name']}/{location['country']}" \
              f" {data['last_updated']} Weather: {data['temp_c']}" \
              f" Celsius, {data['condition']['text']}"
    print(weather)


if __name__ == "__main__":
    get_weather()
