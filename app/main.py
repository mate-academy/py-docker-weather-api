from os import environ
import requests


KEY = environ.get("API_KEY")

CITY = "Paris"

URL = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(URL, params={"q": CITY, "key": KEY})

    response_json = response.json()

    weather_data = response_json.get("current")
    location_data = response_json.get("location")

    result = (
        f"{location_data.get('name')}/"
        f"{location_data.get('country')}"
        f" {location_data.get('localtime')}"
        f" Weather: {weather_data.get('temp_c')} Celsius,"
        f" {weather_data.get('condition').get('text')}"
    )
    print(result)


if __name__ == "__main__":
    get_weather()
