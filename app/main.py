import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY,
                                         "q": CITY}).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    temperature = response["current"]["temp_c"]
    date = response["location"]["localtime"]
    temp_feel_like = response["current"]["feelslike_c"]
    humidity = response["current"]["humidity"]
    wind_report = response["current"]["wind_mph"]

    print(f"Country: {country}")
    print(f"City: {city}")
    print(f"Date: {date}")
    print(f"Temperature: {temperature}")
    print(f"Feel Like: {temp_feel_like}")
    print(f"Humidity: {humidity}")
    print(f"Wind Speed: {wind_report}")


if __name__ == "__main__":
    get_weather()
