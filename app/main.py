import requests
from dotenv import load_dotenv
import os

CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY environment variable not set")

    params = {"key": api_key, "q": CITY}

    response = requests.get(URL, params=params)
    data = response.json()
    if response.status_code != 200:
        raise Exception(response.text)

    print(f"{data['location']['name']}/{data['location']['country']}",
          f"\nlocaltime: {data['location']['localtime']}",
          f"\nWeather: {data['current']['temp_c']} C, "
          f"\nHumidity: {data['current']['humidity']}"
          f"\nCondition: {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
