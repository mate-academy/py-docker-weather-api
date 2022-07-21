import os

import requests


def get_weather():
    key = os.getenv("API_KEY")
    data = requests.get(f"http://api.weatherapi.com/v1/current.json?key={key}&q=Paris").json()
    print("Performing request to Weather API for city Paris...")
    print(f"Paris/France {data['location']['localtime']} "
          f"Weather: {data['current']['temp_c']} Celsius, "
          f"{data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()

