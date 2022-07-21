import os
import requests

key = os.environ["API_WEATHER_KEY"]


def get_weather():
    print(key)
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q=Paris&aqi=no"
    response = requests.get(url)
    jdata = response.json()
    print(f"Temperature in Paris is {jdata['current']['temp_c']} C")


if __name__ == "__main__":
    get_weather()
