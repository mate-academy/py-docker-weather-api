import os
import requests


def get_weather() -> None:
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        raise ValueError("API_KEY not set")
    URL = "http://api.weatherapi.com/v1/current.json"
    PARAMS = {
        "key": API_KEY,
        "q": "Paris"
    }
    RESULT = requests.get(URL, params=PARAMS)
    DATA = RESULT.json()
    TEMP_C = DATA["current"]["temp_c"]
    CONDITION = DATA["current"]["condition"]["text"]
    print(f"Weather in Paris: {TEMP_C}°C, {CONDITION}")


if __name__ == "__main__":
    get_weather()
