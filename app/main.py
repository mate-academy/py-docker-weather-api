import os
import requests
from datetime import datetime


def get_weather() -> None:
    city = "Paris"
    api_key = os.environ.get("API_KEY")
    api_url = (
        f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    )

    try:
        response = requests.get(api_url)
        data = response.json()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        weather_text = (
            f"{city}/France {current_time}"
            f" Weather: {data['current']['temp_c']}"
            f" Celsius, {data['current']['condition']['text']}"
        )
        print(weather_text)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()
