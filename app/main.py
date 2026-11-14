import requests
import os


BASE_URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.getenv("API_KEY")
FILTERING = "Paris"


def get_weather() -> None:
    result = requests.get(BASE_URL + f"key={API_KEY}" + f"&q={FILTERING}")
    result.raise_for_status()
    data = result.json()
    country = data["location"]["country"]
    city = data["location"]["name"]
    date = data["location"]["localtime"]
    temp_celsius = data["current"]["temp_c"]
    weather_condition = data["current"]["condition"]["text"]
    print(
        f"{country}/{city} - {date}\n"
        f"Weather: {temp_celsius} Celsius: {weather_condition}"
    )


if __name__ == "__main__":
    get_weather()
