import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    request = requests.get(
        API_URL,
        params={
            "key": API_KEY,
            "q": CITY,
            "units": "metric"
        }
    )

    if request.status_code == 200:
        data = request.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        local_time = data["location"]["localtime"]
        last_updated = data["current"]["last_updated"]
        temp_c = data["current"]["temp_c"]
        feelslike_c = data["current"]["feelslike_c"]
        weather_condition = data["current"]["condition"]["text"]
        wind_speed = data["current"]["wind_kph"]

        print(
            "\nWeather API\n"
            f"\nLocation\n"
            f"Country: {country}\n"
            f"City: {city}\n"
            f"Local Time: {local_time}\n"
            f"\nWeather\n"
            f"Last Updated: {last_updated}\n"
            f"Condition: {weather_condition}\n"
            f"Temp°C: {temp_c} (feels like {feelslike_c})\n"
            f"Wind Speed: {wind_speed} kph\n"
        )
    else:
        print(f"(Status code: {request.status_code}) " + request.json()["error"]["message"])


if __name__ == "__main__":
    get_weather()
