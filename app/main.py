import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"


def get_weather() -> None:
    response = requests.get(URL)

    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Location: {city}, {country}. "
          f"Weather is {condition}. "
          f"Air temperature: {temp} degrees Celsius")


if __name__ == "__main__":
    get_weather()
