import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
FILTERING = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTERING}
    response = requests.get(URL, params=params).json()
    error = response.get("error")
    if error:
        print(error)
        return
    print(f"Country: {response.get('location').get('country')}\n"
          f"City: {response.get('location').get('name')}\n"
          f"Date: {response.get('location').get('localtime')}\n"
          f"Temperature: {response.get('current').get('temp_c')} Celsius\n"
          f"Weather: {response.get('current').get('condition').get('text')}")


if __name__ == "__main__":
    get_weather()
