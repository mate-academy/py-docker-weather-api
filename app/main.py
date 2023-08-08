import requests
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"

PARAMS = {
    "q": FILTERING,
    "key": API_KEY,
}


def get_weather() -> None:
    result = requests.get(URL, params=PARAMS).json()

    weather = result["current"]["condition"]["text"]
    temperature = result["current"]["temp_c"]

    print(
        f"Weather in Paris: {weather}, Temperature: {temperature}°C"
    )


if __name__ == "__main__":
    get_weather()
