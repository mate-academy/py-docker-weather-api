import os
import requests


API_KEY = os.getenv("API_KEY")
CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "q": CITY,
        "key": API_KEY,
        "lang": "en"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"{data['location']['tz_id']} {data['location']['localtime']} "
              f"Weather: {data['current']['temp_c']} Celsius, "
              f"{data['current']['condition']['text']}")
    else:
        print("Error:", response.status_code)


if __name__ == "__main__":
    print("Performing request to Weather API for city Paris...")
    get_weather()
