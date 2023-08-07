import os
import requests

from dotenv import load_dotenv


load_dotenv()

CITY = "Paris"
API_KEY = os.environ.get("API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "q": CITY,
        "key": API_KEY,
    }

    res = requests.get(URL, params=params)
    data = res.json()
    city = data["location"]["name"]
    region = data["location"]["region"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    condition = data["current"]["condition"]["text"]
    temp_c = data["current"]["temp_c"]
    wind_kph = data["current"]["wind_kph"]
    wind_degree = data["current"]["wind_degree"]
    humidity = data["current"]["humidity"]

    print(
        f"""Weather at local time: {localtime} in {country}({region}) in {city}:
            - Condition: {condition},
            - Air temperature(in Celsius): {temp_c}°C,
            - Wind rate: {wind_kph} kph,
            - Wind direction: {wind_degree}°
            - Air humidity: {humidity}%"""
    )


if __name__ == "__main__":
    get_weather()
