import os
import requests


def get_weather() -> None:
    api_key = os.getenv("WEATHER_API_KEY")
    url = "http://api.weatherapi.com/v1/current.json"
    response = requests.get(url, params={"key": api_key, "q": "Paris"})
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
