import os
import requests


def get_weather() -> None:
    URL = "http://api.weatherapi.com/v1/current.json"
    FILTERING = {
        "key": os.getenv("API_KEY"),
        "q": "Paris"
    }
    response = requests.get(URL, params=FILTERING)
    weather = response.json()
    city = weather["location"]["name"]
    temp = weather["current"]["temp_c"]
    print(f"City: {city} \nTemperature: {temp}°C")


if __name__ == "__main__":
    get_weather()
