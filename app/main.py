from dotenv import load_dotenv
import requests
import os


load_dotenv()
API_KEY=os.getenv("API_KEY")

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    location = data.get("location", {})
    city = location.get("name")
    country = location.get("country")
    localtime = location.get("localtime")
    weather = data.get("current", {})
    temperature = weather.get("temp_c")
    weather = data.get("current", {}).get("condition").get("text")
    print(f"{city}/{country} {localtime} Weather: {temperature} Celsius, {weather}")


if __name__ == "__main__":
    get_weather()
