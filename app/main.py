import os
import requests
from dotenv import load_dotenv

load_dotenv()
URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": CITY}

    print(f"Weather report for {CITY}")

    response = requests.get(URL, params=params)
    print(response)

    if response.status_code == 200:
        weather_data = response.json()

        print(f"Detail information about {weather_data['location']['tz_id']}")
        print(f"Exact time: {weather_data['location']['localtime']}")
        print(f"It is {weather_data['current']['condition']['text']} now")
        print(f"Temperature: {weather_data['current']['temp_c']} Celsius")
    else:
        print("Uuuupsss. Can't get information")


if __name__ == "__main__":
    get_weather()
