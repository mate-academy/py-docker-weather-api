import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"
FILTERING = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API Key not found. "
                         "Set up your API_KEY environment variable.")

    params = {
        "key": API_KEY,
        "q": FILTERING
    }

    try:
        res = requests.get(f"{BASE_URL}/current.json", params=params)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return

    data = res.json()
    location = data.get("location", "N/A")
    weather = data.get("current", "N/A")
    city = location.get("name", "N/A")
    country = location.get("country", "N/A")
    temp_c = weather.get("temp_c", "N/A")
    temp_feels_c = weather.get("feelslike_c", "N/A")
    humidity = weather.get("humidity", "N/A")
    condition = weather.get("condition", "N/A")
    condition_text = condition.get("text", "N/A")

    print(f"Current weather in {city}, {country}: {temp_c}°C "
          f"(feels like {temp_feels_c}°C), {condition_text}, "
          f"with humidity at {humidity}%.")


if __name__ == "__main__":
    get_weather()
