import os

import requests
import json

city = "Paris"
API_KEY = os.environ["API_KEY"]

url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"


def get_weather():
    weather = requests.get(url)
    weather_dict = json.loads(weather.text)
    city = weather_dict['location']['name']
    country = weather_dict['location']['country']
    time = weather_dict['location']['localtime']
    temperature = weather_dict['current']['temp_c']
    condition = weather_dict['current']['condition']['text']

    print(f"Performing request to Weather API for city {city}...")
    print(f"{city}/{country} {time} Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
