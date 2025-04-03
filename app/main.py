import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    KEY = API_KEY
    CITY = "Paris"

    URL = f"http://api.weatherapi.com/v1/current.json?key={KEY}&q={CITY}&aqi=no"

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()

        country = data["location"]["country"]
        date = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        weather_description = data["current"]["condition"]["text"]

        print(f"{CITY}/{country} {date} Weather: {temperature} Celsius, {weather_description}")

    else:
        print("Error fetching the weather data.")


if __name__ == "__main__":
    get_weather()
