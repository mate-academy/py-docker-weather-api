import os
import requests
from dotenv import load_dotenv


load_dotenv()
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Kyiv"
API_KEY = os.environ.get("WEATHER_API_KEY")


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"{data['location']['country']}, "
              f"{data['location']['name']} "
              f"{data['location']['localtime']}, \n"
              f"Current temperature: {data['current']['temp_c']} °C\n"
              f"Feels like: {data['current']['feelslike_c']} °C\n"
              f"Wind speed: {data['current']['wind_kph']} km/h\n"
              f"Current condition: {data['current']['condition']['text']}")
    else:
        print(f"Failed to retrieve weather data. "
              f"Status Code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
