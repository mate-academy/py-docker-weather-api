import requests
import os

API_KEY = os.getenv("API_KEY")
URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&"
FILTERING = "Paris"

def get_weather() -> None:

    res = requests.get(URL + f"q={FILTERING}")
    res_normal = res.json()

    location = res_normal["location"]["name"]
    country = res_normal["location"]["country"]
    localtime = res_normal["location"]["localtime"]

    temp_c = res_normal["current"]["temp_c"]
    condition = res_normal["current"]["condition"]["text"]

    print(f"{location}/{country} {localtime} Weather: {temp_c} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
