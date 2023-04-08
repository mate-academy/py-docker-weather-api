import os
import requests


def get_weather() -> None:
    API_KEY = os.environ.get("API_KEY")
    CITY = "Paris"
    URL = "http://api.weatherapi.com/v1/current.json?"

    response = requests.get(f"{URL}key={API_KEY}&q={CITY}")
    data = response.json()

    if response.ok:
        print(f"Performing request to Weather API for city {CITY}...")
        location = data.get("location")
        current = data.get("current")
        print(
            f"{location.get('name')}/{location.get('country')} "
            f"{location.get('localtime')} Weather: {current.get('temp_c')} "
            f"Celsius, {current.get('condition').get('text')}"
        )
    else:
        print("Error: ", response.status_code)


if __name__ == "__main__":
    get_weather()
