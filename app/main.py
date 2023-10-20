import os

import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    if API_KEY is None:
        print("API_KEY is not set. Please set it before running the script.")
        return

    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": "no"
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]

        wind_dir = data["current"]["wind_dir"]
        wind_speed = data["current"]["wind_kph"]
        percentage_of_cloud = data["current"]["cloud"]
        percentage_of_air_humidity = data["current"]["humidity"]

        print(f"Current location: {city}/{country}\n"
              f"Local time: {local_time}\n"
              f"Wind direction: {wind_dir}\n"
              f"Wind speed: {wind_speed} km/hour\n"
              f"Cloudiness: {percentage_of_cloud}%\n"
              f"Air Humidity: {percentage_of_air_humidity}%")

    else:
        print(
            f"Sorry, your token is not valid."
            f" Regenerate it and come again! Status code: {response.status_code}"
        )


if __name__ == "__main__":
    get_weather()
