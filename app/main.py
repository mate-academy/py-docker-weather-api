import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
api_key = os.environ.get("API_KEY")


def get_weather() -> None:
    params = {
        "key": api_key,
        "q": CITY
    }
    response = requests.get(URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    temp = data.get("current").get("temp_c")
    condition = data.get("current").get("condition").get("text")
    print(f"Weather in {CITY}:"
          f"\nTemperature: {temp}"
          f"\nCondition: {condition}")


if __name__ == "__main__":
    get_weather()
