import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY", "django-insecure-jgd9@7+bs^s%cq-!zyp")

CITY = "Paris"


def get_weather() -> None:
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        country = weather_data["location"]["country"]
        city = weather_data["location"]["name"]
        localtime = weather_data["location"]["localtime"]
        temp_c = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        weather = (
            f"{country}/{city} {localtime}"
            f"Weather: {temp_c} Celsius, {condition}"
        )
        print(weather)
    else:
        print(
            f"Error code: {response.status_code}"
            f", {response.text.split(',')[1][:-2]}"
        )


if __name__ == "__main__":
    get_weather()
