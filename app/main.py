import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Kyiv"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTERING,
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()

        city = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"The weather in {city}: ")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")


if __name__ == "__main__":
    get_weather()
