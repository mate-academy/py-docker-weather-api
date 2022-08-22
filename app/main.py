import os
import requests


API_KEY = os.environ.get("API_KEY")
CITY_NAME = "Paris"


url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY_NAME}&aqi=no"


def get_weather():
    response = requests.get(url)
    status_code = requests.get(url).status_code
    weather_in_city = response.json()["current"]

    if status_code == 200:
        current_temperature = weather_in_city["temp_c"]
        print(f"Temperature in {CITY_NAME} {current_temperature} °С")
    else:
        print("Сheck that you entered all the data correctly")


if __name__ == "__main__":
    get_weather()
