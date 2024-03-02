import os
import requests
from datetime import datetime


def get_weather() -> None:
    FILTERING = "Paris"
    API_KEY = os.environ.get("API_KEY")
    URL = "http://api.weatherapi.com/?"

    params = {"key": API_KEY, "q": FILTERING}

    try:
        response = requests.get(url=URL, params=params)
        data = response.json()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        weather_text = (
            f"{FILTERING}/France {current_time}"
            f" Weather: {data['current']['temp_c']}"
            f" Celsius, {data['current']['condition']['text']}"
        )
        print(weather_text)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()
