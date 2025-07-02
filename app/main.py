import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "London"
    url = (f"https://api.weatherapi.com/v1/current.json?"
           f"key={api_key}&q={city}&aqi=no")
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        print(f"Weather in {city}: {data["current"]["condition"]["text"]}, "
              f"Temp: {data["current"]["temp_c"]}°C")
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")


if __name__ == "__main__":
    get_weather()
