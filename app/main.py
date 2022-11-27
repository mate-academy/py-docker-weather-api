import os

import requests


URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL + f"key={API_KEY}&q={CITY}")

    if response.status_code == 200:
        data = response.json()

        weather = {
            "City": data["location"]["name"],
            "Temperature": data["current"]["temp_c"],
            "Feels like": data["current"]["feelslike_c"],
            "Condition": data["current"]["condition"]["text"],
            "Wind gust": data["current"]["gust_kph"]
        }

        for keys, values in weather.items():
            print(f"{keys}: {values}")
    else:
        print("400 - Bad request")


if __name__ == "__main__":
    get_weather()
