import os
import requests


CITY = "Paris"
API_KEY = os.getenv("API_KEY")
url = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": "no"
    }

    response = requests.get(url, params)
    data = response.json()

    city = data["location"]["name"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"City: {city}, Temperature: {temp}, Condition: {condition}")


if __name__ == "__main__":
    get_weather()
