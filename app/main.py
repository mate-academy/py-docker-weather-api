import os

import requests

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"

def get_weather() -> None:
    url = f"{BASE_URL}key={API_KEY}&q={FILTERING}"
    res = requests.get(url).json()
    print(f"The temperature in {FILTERING} is "
          f"{res['current']['temp_c']} degrees Celsius")


if __name__ == "__main__":
    get_weather()
