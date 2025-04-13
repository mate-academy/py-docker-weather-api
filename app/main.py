import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city="Paris"):
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = f"{BASE_URL}?key={api_key}&q={city}"
    response = requests.get(url)
    data = response.json()

    location = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    localtime = data["location"]["localtime"]

    print(f"{location}/{country} {localtime} Weather: {temp_c} Celsius, {condition}")

if __name__ == "__main__":
    get_weather()
