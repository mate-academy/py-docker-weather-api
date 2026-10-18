import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
city = "Paris"
api_key = os.environ.get("API_KEY")


def get_weather() -> None:
    params = {
        "key": api_key,
        "q": city
    }
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    temp = data.get("current").get("temp_c")
    condition = data.get("current").get("condition").get("text")
    print(f"Weather in {city}:"
          f"\nTemperature: {temp}"
          f"\nCondition: {condition}")


if __name__ == "__main__":
    get_weather()
