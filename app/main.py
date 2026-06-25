import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
    }
    response = requests.get(URL, params=params)
    data = response.json()

    city = data["location"]["name"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(
        f"Weather in {city}: "
        f"{temp}°C, "
        f"{condition}"
    )


if __name__ == "__main__":
    get_weather()
