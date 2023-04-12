import os
import requests


API_KEY = os.environ.get("WEATHER_API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": FILTERING}
    result = requests.get(URL, params=params)
    info = result.json()

    if "location" in info:
        country = info["location"]["country"]
        city = info["location"]["name"]
        temp = info["current"]["temp_c"]
        condition = info["current"]["condition"]["text"]
        print(
            f"In {city} ({country}) the weather is - {condition} and"
            f" temperature now is {temp}°"
        )
    else:
        print("Location information not available.")


if __name__ == "__main__":
    get_weather()
