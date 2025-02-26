import os
import requests

from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    print("Performing request to Weather API for city Paris ...")
    url = f"https://api.weatherapi.com/v1/current.json?key={os.getenv('API_KEY')}&q=Paris&aqi=yes"
    response = requests.get(url).json()
    city = response["location"]["name"]
    country = response["location"]["country"]
    time_date = response["location"]["localtime"]
    weather = response["current"]["temp_c"]
    status = response["current"]["condition"]["text"]
    return print(f"{city}/{country} {time_date} Weather: {weather} Celsius {status}")


if __name__ == "__main__":
    get_weather()
