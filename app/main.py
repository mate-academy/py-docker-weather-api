import os

import requests

URL = "http://api.weatherapi.com/v1/timezone.json?q="
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    result = requests.get(URL + CITY + f"&key={API_KEY}")
    data = result.json()
    print(
        f"City: {data['location']['name']}, "
        f"Regin: {data['location']['region']}, "
        f"Coutry: {data['location']['country']} "
        f"Time Zone: {data['location']['tz_id']}"
    )

if __name__ == "__main__":
    get_weather()
