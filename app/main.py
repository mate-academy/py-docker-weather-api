import os
import requests


URL = "http://api.weatherapi.com/v1/current.json/?"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL + f"q={FILTERING}")

    if response.status_code == 200:
        data = response.json()
        main = data["main"]
        temperature = main["temp_c"]
        temp_feel_like = main["feelslike_c"]
        humidity = main["humidity"]
        pressure = main["pressure_mb"]
        wind_report = data["gust_kph"]

        print(f"Temperature: {temperature}")
        print(f"Feel Like: {temp_feel_like}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Wind Speed: {wind_report['speed']}")
    else:
        print("Error in the HTTP request")


if __name__ == "__main__":
    get_weather()
