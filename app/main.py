import os
import requests
from requests import ConnectionError

API_ENDPOINT = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Odesa"


def get_full_url(endpoint: str, api_key: str, city: str) -> str:
    return f"{endpoint}?key={api_key}&q={city}&aqi=no"


def get_weather() -> None:
    try:
        res = requests.get(get_full_url(API_ENDPOINT, API_KEY, CITY)).json()

        location = res["location"]
        current = res["current"]

        print(
            f"And now for the weather in "
            f"{location['region']}, {location['country']}:\n"
            f"Temperature is {current['temp_c']} Celsius. "
            f"Feels like {current['feelslike_c']} degrees.\n"
            f"It's {(current['condition']['text'].lower())} now.\n"
            f"Wind speed is {current['wind_kph']} km/h."
        )

    except ConnectionError:
        print("Something went wrong with your connection. Try again later.")


if __name__ == "__main__":
    get_weather()
