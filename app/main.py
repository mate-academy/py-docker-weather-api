import os

import requests
from dotenv import load_dotenv


load_dotenv()


FILTERING_CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"
KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(f"{BASE_URL}?key={KEY}&q={FILTERING_CITY}")

    if response.status_code == 200:
        info = response.json()
        city_name = info["location"]["name"]
        country = info["location"]["country"]
        localtime = info["location"]["localtime"]
        temp_c = info["current"]["temp_c"]
        print(f"City: {city_name}, "
              f"Country: {country}, "
              f"Local Time: {localtime}, "
              f"Temperature: {temp_c}°C")
    else:
        return print(f"Failed to find data, code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
