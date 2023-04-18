import os
import requests

API_KEY = os.environ.get("WEATHER_API_KEY")
URL = "https://api.weatherapi.com/v1/current.json"
LOCATION = "Paris"


def get_weather() -> None:
    params = {"key": API_KEY, "q": LOCATION}
    result = requests.get(URL, params=params)
    info = result.json()

    if "location" in info:
        country = info["location"]["country"]
        city = info["location"]["name"]
        temperature = info["current"]["temp_c"]
        condition = info["current"]["condition"]["text"]
        print(
            f"In {city} ({country}) the weather is - {condition} and"
            f" temperature now — {temperature}° Celsius"
        )
    else:
        print(f"Information about weather in {LOCATION} is not available.")


if __name__ == "__main__":
    get_weather()
