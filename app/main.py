import os
import requests

WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Paris"


def get_weather():
    res = requests.get(WEATHER_API_URL, {
        "key": API_KEY,
        "q": CITY,
    }).json()
    print(f"City: {CITY}; Current temperature: {res['current']['temp_c']} Celsius; "
          f"Local time: {res['location']['localtime']}; "
          f"Condition: {res['current']['condition']['text']};")


if __name__ == "__main__":
    get_weather()
