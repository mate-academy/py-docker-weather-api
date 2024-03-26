import os

import requests


API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}

    try:
        data = requests.get(URL, params).json()
        country = data["location"]["country"]
        time = data["current"]["last_updated"]
        temperature = data["current"]["temp_c"]
        weather = data["current"]["condition"]["text"]

        print(
            f"Country: {country}\n"
            f"City: Paris\n"
            f"Time: {time}\n"
            f"Temperature: {temperature}\n"
            f"Weather: {weather}"
        )
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    get_weather()
