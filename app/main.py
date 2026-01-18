import os
import requests


CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    url = f"{BASE_URL}?key={api_key}&q={CITY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"{name}/current weather: {temp_c} Celsius, {condition}")
    else:
        print(f"Error fetching weather: {response.status_code}")


if __name__ == "__main__":
    get_weather()
