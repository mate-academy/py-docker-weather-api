import os
import requests
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
API_URL = "https: //api.weatherapi.com/v1/current.json"
CITY = "Paris"
AQI = "no"


def get_weather() -> None:
    response = requests.get(
        f"https: //API_URL"
        f"key={SECRET_KEY}&q={CITY}&aqi={AQI}"
    )
    print(response.json())


if __name__ == "__main__":
    get_weather()
