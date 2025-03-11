import os
import requests

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"

def get_weather() -> None:
    print(f"Performing request to Weather API for city {FILTERING}...")
    url = URL + f"key={API_KEY}" + f"&q={FILTERING}"
    response = requests.get(url)
    dict_resp_weather = response.json()
    country = dict_resp_weather["location"]["country"]
    localtime = dict_resp_weather["location"]["localtime"]
    temperature = dict_resp_weather["current"]["temp_c"]
    condition = dict_resp_weather["current"]["condition"]["text"]
    print(f"{FILTERING}/{country} {localtime} Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
