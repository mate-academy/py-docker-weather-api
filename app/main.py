import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("WEATHER_API_KEY")


def get_weather() -> None:
    response = requests.get(URL,
                            params={"key": API_KEY,
                                    "q": CITY,
                                    "aqi": "no"})
    if response.status_code == 200:
        data = response.json()
        print(f"{data['location']['localtime']}, {data['location']['name']}, {data['location']['country']}\n"
              f"current temperature: {data['current']['temp_c']}C"
              f"{data['current']['condition']['text']}")
    else:
        print(f"Failed to retrieve weather data. Status Code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
