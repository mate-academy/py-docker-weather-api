import requests

import os


def get_weather():
    api_key = os.environ.get("API_KEY")
    request_data = requests.get(f"https://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris").json()
    print("The weather in Paris is: \n"
          f"{request_data['location']['name']}/"
          f"{request_data['location']['country']}"
          f" {request_data['location']['localtime']}"
          f" Weather: {request_data['current']['feelslike_c']} Celsium,"
          f" {request_data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
