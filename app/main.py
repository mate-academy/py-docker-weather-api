import os
import requests


API_KEY = os.environ.get("API_KEY")

if not API_KEY:
    raise ValueError("Environmental variable 'API_KEY' has not been set.")

CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:

    params = {
        "q": CITY,
        "key": API_KEY,
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"The weather in {CITY}: {condition}, temperature: {temp}°C.")
    else:
        print(f"Error: {response.status_code}, {response.text}.")


if __name__ == "__main__":
    get_weather()
