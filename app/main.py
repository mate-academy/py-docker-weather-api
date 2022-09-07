import requests

import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
base_url = "https://api.weatherapi.com/v1/current.json?"
city_name = "Paris"


def get_weather():

    complete_url = base_url + "key=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)

    result = response.json()
    current_temperature = int(result["current"]["temp_c"])

    print(f"Temperature in {city_name} is {current_temperature} degrees now.")


if __name__ == "__main__":
    get_weather()
