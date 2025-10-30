from dotenv import load_dotenv
import os
import requests


load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q=Paris&aqi=no"

def get_weather() -> None:
    response = requests.get(URL)
    data = response.json()
    condition = data["current"]["condition"]["text"]
    print(condition)

if __name__ == "__main__":
    get_weather()
