import os
from dotenv import load_dotenv
import requests

load_dotenv()

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"
PARAMS = {
    "key": API_KEY,
    "q": CITY,
}


def get_weather() -> None:
    request = requests.get(url=URL, params=PARAMS)

    if request.status_code == 200:
        data = request.json()

        location = data.get("location")
        current = data.get("current")

        city = location["name"]
        country = location["country"]
        localtime = location["localtime"]
        temp = current["temp_c"]
        condition = current["condition"]["text"]

        weather_string = (
            f"{city}/{country} {localtime} "
            f"Weather: {temp} Celsius, {condition}"
        )

        print(weather_string)

    return request.status_code


if __name__ == "__main__":
    get_weather()
