import os
import requests

API_KEY = os.getenv("API_KEY")
CITY = "Paris"
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"

def get_weather():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {CITY}: {data['current']['temp_c']}°C, {data['current']['condition']['text']}")
    else:
        print("Error fetching weather data:", response.text)

if __name__ == "__main__":
    get_weather()
