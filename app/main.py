from dotenv import load_dotenv
import os
import requests


load_dotenv()
api_key = os.getenv("API_KEY")
if not api_key:
    print("Error: API_KEY is missing")
    exit(1)

URL = "https://api.weatherapi.com/v1/current.json"
params = {
    "key": api_key,
    "q": "Paris"
}
response = requests.get(url=URL, params=params)
data = response.json()


def get_weather(data: dict) -> None:
    location = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_kph"]
    condition = data["current"]["condition"]["text"]

    print(f"The weather in {location}, temperature: {temperature},"
            f"humidity: {humidity}, wind speed: {wind_speed},"
            f"condition: {condition}")


if __name__ == "__main__":
    get_weather(data)
