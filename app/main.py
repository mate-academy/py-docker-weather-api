import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": "Paris",
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()

    if response.status_code == 200:
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")
    else:
        print("Failed to retrieve weather data.")


if __name__ == "__main__":
    get_weather()
