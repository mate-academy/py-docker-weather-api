import requests
import os


api_key = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
PARAMS = {"key": api_key, "q": CITY}


def get_weather() -> None:
    response = requests.get(URL, params=PARAMS)

    data = response.json()
    current_location = data['location']['name']
    current_temp = data['current']['temp_c']

    print(f"Current weather in {current_location}: {current_temp}°C")


if __name__ == "__main__":
    get_weather()
