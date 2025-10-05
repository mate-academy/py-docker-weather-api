import os
import requests
from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    params = {"key": api_key, "q": "Paris"}
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params=params
    )
    data = response.json()
    location = data["location"]
    current = data["current"]
    condition = current["condition"]
    message = (
        f"{location['name']}/{location['country']} "
        f"{location['localtime']} "
        f"Weather: {current['temp_c']}°C, {condition['text']}"
    )
    print(message)


if __name__ == "__main__":
    get_weather()
