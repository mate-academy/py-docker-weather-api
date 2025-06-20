import requests
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")

    params = {
        "q": "Cherkasy",
        "key": API_KEY
    }

    url = "http://api.weatherapi.com/v1/current.json"

    response = requests.get(url, params=params)
    country = response.json()["location"]["country"]
    location = response.json()["location"]["name"]
    temp = response.json()["current"]["temp_c"]
    time = response.json()["location"]["localtime"]

    print(f'{country}/{location} - {time}, Weather: {temp} Celsius')

if __name__ == "__main__":
    get_weather()
