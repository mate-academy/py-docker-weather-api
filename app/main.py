import os
import requests
from dotenv import load_dotenv
load_dotenv()


BASE_URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather(city: str = CITY, api_key: str = API_KEY) -> print:

    response = requests.get(
        url=BASE_URL, params={"key": api_key, "q": city}
    ).json()

    city = response["location"]["name"]
    region = response["location"]["region"]
    country = response["location"]["country"]
    current_time = response["location"]["localtime"]
    weather = response["current"]["temp_c"]
    wind = response["current"]["wind_mph"]
    condition = response["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...\n\n")
    print(f"{city}\n{region}\n{country}\n\n"
          f"Temperature: {weather}\n"
          f"Wind speed: {wind}\n"
          f"Condition: {condition}\n{current_time}")
    print("Have a nice day!")


if __name__ == "__main__":
    get_weather()
