import os
import requests
from dotenv import load_dotenv
load_dotenv()


BASE_URL = "http://api.weatherapi.com/v1/current.json?"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather(city: str = CITY, appi_key: str = API_KEY) -> print:

    response = requests.get(
        url=BASE_URL, params={"key": appi_key, "q": city}
    ).json()

    get_city = response["location"]["name"]
    get_region = response["location"]["region"]
    get_country = response["location"]["country"]
    get_current_time = response["location"]["localtime"]
    get_weather = response["current"]["temp_c"]
    get_wind = response["current"]["wind_mph"]
    get_condition = response["current"]["condition"]["text"]

    print(f"Performing request to Weather API for city {city}...\n\n")
    print(f"{get_city}\n{get_region}\n{get_country}\n\n"
          f"Temperature: {get_weather}\n"
          f"Wind speed: {get_wind}\n"
          f"Condition: {get_condition}\n{get_current_time}")
    print("Have a nice day!")


if __name__ == "__main__":
    get_weather()
