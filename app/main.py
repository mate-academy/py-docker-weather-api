import os

import requests

CITY = "PARIS"
API_KEY = os.environ.get('API_KEY')

def get_weather():
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # перевіряє статус-код (200-299)
        data = response.json()
        # тут парсимо і виводимо погоду
        print(f"Current temperature in {CITY}: {data['current']['temp_c']}°C")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    get_weather()

