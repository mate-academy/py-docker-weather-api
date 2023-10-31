import os

import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    payload = {"key": API_KEY, "q": CITY}
    result = requests.get(BASE_URL, params=payload)

    if result.status_code == 200:
        data = result.json()
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temperature = data["current"]["temp_c"]
        text = data["current"]["condition"]["text"]

        print(
            f"Country: {country}, "
            f"City: {CITY}, "
            f"Localtime: {localtime}, "
            f"Temperature: {temperature}°С "
            f"{text}"
        )
    else:
        print(f"Bad request: {resource.status_code}")


if __name__ == "__main__":
    get_weather()
