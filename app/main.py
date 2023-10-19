import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def weather():
    if not API_KEY:
        raise ValueError("Weather API key is not provided")

    url = f"{BASE_URL}?q={CITY}&key={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country = data["location"]["country"]
        city = data["location"]["name"]
        region = data["location"]["region"]
        condition = data["current"]["condition"]["text"]
        temperature = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        print(
            f"Location: {country}, {region}, {city}\n"
            f"Condition: {condition}\n"
            f"Air temperature: {temperature}°C\n"
            f"Feels like: {feels_like}°C\n"
        )
    else:
        print("Failed to retrieve weather data")


if __name__ == "__main__":
    weather()
