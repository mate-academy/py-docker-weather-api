import os
import requests

from dotenv import load_dotenv

load_dotenv()

WEATHER_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY environment variable not set.")
    else:
        try:
            url = f"{WEATHER_URL}?key={api_key}&q={CITY}"
            response = requests.get(url)

            if response.status_code == 200:
                weather_data = response.json()

                country = weather_data["location"]["country"]
                localtime = weather_data["location"]["localtime"]
                temperature = weather_data["current"]["temp_c"]
                condition = weather_data["current"]["condition"]["text"]

                print(f"Performing requests to Weather API for city {CITY}...")
                print(f"{CITY}/{country} {localtime} - {temperature}°C, "
                      f"{condition}")
            else:
                print("Failed to get weather data")

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")


if __name__ == "__main__":
    get_weather()
