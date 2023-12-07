import os
import requests
from dotenv import load_dotenv

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": FILTERING
        }
    )
    if response.status_code == 200:
        resp = response.json()
        print(
            f"{resp['location']['name']}/{resp['location']['country']}"
            f" {resp['location']['localtime']} Weather: {resp['current']['temp_c']}"
            f" Celsius, {resp['current']['condition']['text']}"
        )
    else:
        print(
            f"Error: status code = {response.status_code}"
        )






if __name__ == "__main__":
    get_weather()
