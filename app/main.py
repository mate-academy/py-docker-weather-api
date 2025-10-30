from dotenv import load_dotenv
import os
import requests


load_dotenv()
API_KEY = os.getenv("API_KEY")
CITY = "Paris"
AQI = "no"
BASE_URL = f"https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    req_url = BASE_URL + f"?key={API_KEY}&q={CITY}&aqi={AQI}"
    response = requests.get(req_url)
    data = response.json()
    condition = data["current"]["condition"]["text"]
    print(condition)

if __name__ == "__main__":
    get_weather()
