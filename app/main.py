import os
import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        print("You don't have api token...\nAccess denied!")
        return

    payload = {"key": API_KEY, "q": CITY}
    request = requests.get(URL, params=payload)

    print(f"Performing request to Weather API for city {CITY}.")

    if request.status_code == 200:
        request_data = request.json()
        location = request_data.get("location")
        weather = request_data.get("current")
        print(
            f"{location.get('name')}/{location.get('country')} "
            f"{location.get('localtime')} "
            f"Weather: {weather.get('temp_c')} Celsius, "
            f"{weather.get('condition').get('text')}"
        )

    else:
        print(f"Bad request: {request.status_code}")


if __name__ == "__main__":
    get_weather()
