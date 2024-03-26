import os
import requests

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
City = "Paris"
LANG = "uk"


def get_weather() -> None:
    response = requests.get(f"{BASE_URL}?key={API_KEY}&q={City}&lang={LANG}")

    if response.status_code == 200:
        response_current = response.json().get("current")
        response_location = response.json().get("location")

        print(
            "\nCurrent weather:\n"
            f"Country: {response_location.get('country')}\n"
            f"City: {response_location.get('name')}\n"
            f"Local datetime: {response_location.get('localtime')}\n"
            f"Cloud: {response_current.get('cloud')}\n"
            f"{response_current.get('condition').get('text')}\n"
            f"Humidity: {response_current.get('humidity')}\n"
            f"Temperature °C: {response_current.get('temp_c')}\n"
            f"Feels like °C: {response_current.get('feelslike_c')}\n"
        )
    else:
        print(f"Status code: {response.status_code}, Reason: {response.reason}")


if __name__ == "__main__":
    get_weather()
