import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
LOCATION = "Paris"
URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={LOCATION}"


def get_weather() -> None:
    response = requests.get(URL)
    data = response.json()

    text = data["current"]["condition"]["text"]
    temp_c = data["current"]["temp_c"]
    temp_f = data["current"]["temp_f"]
    feels = data["current"]["feelslike_c"]
    last_updated = data["current"]["last_updated"]
    gust_kph = data["current"]["gust_kph"]
    pressure_in = data["current"]["pressure_in"]
    humidity = data["current"]["humidity"]

    print(
        f"Current weather in {LOCATION}, country France:\n"
        f"{text}. "
        f"Temperature in °C: {temp_c}°C "
        f"Temperature in °F: {temp_f}°F \n"
        f"Feels like: {feels}°C.\n"
        f"Last updated: {last_updated} \n"
        f"Wind: {gust_kph} km/h \n"
        f"Humidity: {humidity}% \n"
        f"Precipitation: {pressure_in} mm \n"
    )


if __name__ == "__main__":
    get_weather()
