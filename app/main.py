import requests
import os

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
FILTER = "Paris"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": FILTER
    }

    response = requests.get(URL, params=params)
    data = response.json()

    location = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    temp_feeling = data["current"]["feelslike_c"]
    condition = data["current"]["condition"]["text"]
    wind = data["current"]["wind_kph"]
    clouds = data["current"]["cloud"]

    print(
        f"Weather in {location}",
        f"Temperature is {temperature} degree, feels like {temp_feeling}",
        f" Condition: {condition}",
        f"Wind is {wind} km/h",
        f"Percentage of clouds is {clouds}"
    )


if __name__ == "__main__":
    get_weather()
