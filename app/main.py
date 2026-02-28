import requests
import os


WEATHER_API_KEY = os.environ.get("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:

    if not WEATHER_API_KEY:
        print("Error: API_KEY is not set.")
        return

    url = f"{BASE_URL}?key={WEATHER_API_KEY}&q={CITY}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        f"{city}/{country} {localtime} Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
