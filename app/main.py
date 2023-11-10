import requests
import os
from dotenv import load_dotenv, find_dotenv


def get_weather() -> None:
    load_dotenv(find_dotenv())
    API_KEY = os.environ["API_KEY"]
    URL = "http://api.weatherapi.com/v1/current.json?"
    FILTERING = "Paris"
    result = requests.get(URL + f"key={API_KEY}" + "&" + f"q={FILTERING}")
    data = result.json()
    location = data['location']['name']
    localtime = data['location']['localtime']
    temp_c = data['current']['temp_c']
    condition = data['current']['condition']['text']
    print(f"{location} {localtime} Weather {temp_c} Celsius {condition}")


if __name__ == "__main__":
    get_weather()
