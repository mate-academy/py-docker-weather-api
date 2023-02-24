import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    url = "http://api.weatherapi.com/v1/current.json?key="
    aqi = "no"
    city_name = "Paris"
    full_url = url + api_key + "&q=" + city_name + "&aqi=" + aqi
    req = requests.get(full_url)
    info = req.json()
    print(
        f"{info['location']['name']}/{info['location']['country']} "
        f"{info['location']['localtime']} "
        f"Weather: {info['current']['temp_c']} Celsius, "
        f"{info['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
