import os
import requests


def get_weather() -> None:
    API_KEY = os.getenv("WEATHER_API_KEY")
    URL = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(URL, params={"key": API_KEY, "q": "Paris"})
    data = response.json()

    place = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(
        f"{place}/{country} {localtime} "
        f"Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":
    get_weather()
