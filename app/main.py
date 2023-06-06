import os

import requests
from dotenv import load_dotenv


def get_weather() -> None:
    response = requests.get(URL)
    data = response.json()

    text = data["current"]["condition"]["text"]
    temp_c = data["current"]["temp_c"]
    feelslike_c = data["current"]["feelslike_c"]
    gust_kph = data["current"]["gust_kph"]
    pressure_in = data["current"]["pressure_in"]
    humidity = data["current"]["humidity"]
    last_updated = data["current"]["last_updated"]

    print(
        f"Current weather in {CITY} at {last_updated}:\n"
        f"{text}. "
        f"Temperature: {temp_c}°C, feels like {feelslike_c}°C.\n"
        f"Wind: {gust_kph} km/h \n"
        f"Humidity: {humidity}% \n"
        f"Precipitation: {pressure_in} mm"
    )


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.environ.get("API_KEY")
    CITY = "Paris"
    URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"
    get_weather()
