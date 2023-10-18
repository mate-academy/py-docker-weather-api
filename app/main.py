import os

import requests


CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/"
API_KEY = os.environ.get("API_KEY")
URL = f"{BASE_URL}current.json?key={API_KEY}&q={CITY}"


def get_weather() -> str:
    response = requests.get(URL).json()
    return (f"The current weather in {CITY}:\n"
            f"Temperature: {response['current']['temp_c']}\n"
            f"Feels like: {response['current']['feelslike_c']}\n"
            f"Wind speed: {response['current']['wind_kph']}\n"
            f"Wind direction: {response['current']['wind_dir']}"
            )


if __name__ == "__main__":
    print(get_weather())
