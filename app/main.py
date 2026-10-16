import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ["API_KEY"]

    params = {
        "key": api_key,
        "q": CITY
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    weather_data = response.json()
    print(f"City: {weather_data["location"]["name"]}")
    print(f"Temperature: {weather_data["current"]["temp_c"]}°C")
    print(f"Condition: {weather_data["current"]["condition"]["text"]}")


if __name__ == "__main__":
    get_weather()
