import os
import requests


BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    url = f"{BASE_URL}?key={api_key}&q={CITY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Current weather in Paris: {temp}°C, {condition}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    get_weather()
