import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        url=URL,
        params={
            "key": API_KEY,
            "q": CITY
        }
    )

    if response.status_code == 200:
        weather_data = response.json()
        temp_c = weather_data["current"]["temp_c"]
        temp_f = weather_data["current"]["temp_f"]
        condition = weather_data["current"]["condition"]["text"]
        wind_kph = weather_data["current"]["wind_kph"]
        wind_dir = weather_data["current"]["wind_dir"]

        print(f"Generating short weather forecast for {CITY}...")
        print(f"Now the weather in {CITY} is {condition}\n"
              f"Temperature by Celsius: {temp_c} C\n"
              f"Temperature by Fahrenheit: {temp_f} F\n"
              f"Wind directory is {wind_dir} with {wind_kph} kph")
    else:
        print("An error occurred while getting response!")
        print(f"Status code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
