import os
import requests

URL_API = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    try:
        res = requests.get(URL_API, params={
            "key": API_KEY,
            "q": CITY,
        }).json()

        locale = res["location"]
        temp = res["current"]

        print(f"{locale['name']}/{locale['country']} "
              f"{locale['localtime']} Weather: {temp['temp_c']} "
              f"Celsius, {temp['condition']['text']}")
    except Exception:
        raise Exception("Something went wrong")


if __name__ == "__main__":
    get_weather()
