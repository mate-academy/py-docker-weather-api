import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

def get_paris_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    response = requests.get(f"{URL}?key={api_key}&q={CITY}")
    response.raise_for_status()
    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Current weather in {city}, {country}:")
    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")

if __name__ == "__main__":
    get_paris_weather()
