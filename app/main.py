import os
import requests


URL = "http://api.weatherapi.com/v1/current.json/?"
API_KEY = os.environ.get("API_KEY")
FILTERING = "Paris"
result = requests.get(URL + f"q={FILTERING}")


def get_weather() -> None:
    try:
        info = result.json()
        location = f"{info['location']['name']}/{info['location']['country']}"
        localtime = info['location']['localtime']
        temperature = info['current']['temp_c']
        condition = info['current']['condition']['text']
        print("Performing request to Weather API for city Paris...")
        print(f"{location} {localtime} Weather: {temperature} Celsius, {condition}")
    except Exception:
        raise Exception("Something went wrong...")


if __name__ == "__main__":
    get_weather()
