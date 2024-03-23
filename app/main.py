import os
import requests

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
City = "Paris"
LANG = "uk"


def get_weather() -> None:
    response = requests.get(
        BASE_URL,
        params={
            "key": API_KEY,
            "q": City,
            "lang": LANG,
        },
    )
    if response.status_code == 200:
        response_current = response.json().get("current")
        response_location = response.json().get("location")

        print("\nCurrent weather:\n")
        print("Country:", response_location.get("country"))
        print("City:", response_location.get("name"))
        print("Local datetime:", response_location.get("localtime"))
        print(
            f"Cloud: {response_current.get('cloud')} "
            f"{response_current.get('condition').get('text')}",
        )
        print("Humidity:", response_current.get("humidity"))
        print("Temperature °C:", response_current.get("temp_c"))
        print("Feels like °C:", response_current.get("feelslike_c"))
    else:
        print("Oops! Something went wrong! :)")


if __name__ == "__main__":
    get_weather()
