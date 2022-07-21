import os

import requests


def get_weather():

    base_url = "https://api.weatherapi.com/v1/current.json?q=Paris&key="

    try:
        api_user = os.getenv("API_KEY", default=None)
        response = requests.get(base_url + api_user).json()
    except TypeError:
        print("you should give an api_key")
        return

    print("Performing request to Weather API for city Paris...")
    print(f'{response["location"]["name"]}/{response["location"]["country"]}'
          f' {response["current"]["last_updated"]}'
          f' Weather: {response["current"]["temp_c"]} Celsius,'
          f' {response["current"]["condition"]["text"]}')


if __name__ == "__main__":
    get_weather()
