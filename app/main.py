import os
import requests
from dotenv import load_dotenv
from datetime import datetime


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is not set.")
        return
    city = "Paris"
    country = "France"
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}" # noqa E231
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        condition = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"]
        print(f"{city}/{country} {current_time} "
              f"Weather: {temperature} Celsius, {condition}")
    else:
        print("Failed to fetch weather data:", response.text)


if __name__ == "__main__":
    get_weather()
