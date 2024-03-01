import os
import requests
from datetime import datetime


def get_weather() -> None:
    filtering = "Paris"
    api_key = os.environ.get("API_KEY")
    url = "http://api.weatherapi.com/?"

    result = requests.get(url + f"key={api_key}&q={filtering}")

    try:
        response = requests.get(result)
        data = response.json()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        weather_text = (
            f"{filtering}/France {current_time}"
            f" Weather: {data['current']['temp_c']}"
            f" Celsius, {data['current']['condition']['text']}"
        )
        print(weather_text)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_weather()
