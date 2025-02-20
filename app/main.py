import requests
import os
from dotenv import load_dotenv
load_dotenv()
def get_weather():
    api_key = os.getenv("API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "Paris",
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Failed to get weather data")
        return None

def print_weather(weather_data):
    if weather_data:
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    else:
        print("No weather data available")

if __name__ == "__main__":
    weather_data = get_weather()
    print_weather(weather_data)
