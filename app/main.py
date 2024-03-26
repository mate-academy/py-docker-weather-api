import os
from dotenv import load_dotenv
import requests
from datetime import datetime


load_dotenv()


BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
LOCATION = "Paris"
URL = f"{BASE_URL}?key={API_KEY}&q={LOCATION}"


def get_weather() -> None:
    response = requests.get(URL)
    if response.status_code == 200:
        weather_data = response.json()
        location_name = weather_data["location"]["name"]
        country = weather_data["location"]["country"]
        current_time = datetime.strptime(
            weather_data["location"]["localtime"],
            "%Y-%m-%d %H:%M"
        )
        temperature_c = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        formatted_time = current_time.strftime("%d-%m-%y %H:%M")
        print(
            f"{location_name}/{country} "
            f"{formatted_time} Weather: "
            f"{temperature_c: .1f} Celsius, {condition}"
        )
    else:
        error_response = response.json()
        print("Error fetching weather data:", error_response)


if __name__ == "__main__":
    get_weather()
