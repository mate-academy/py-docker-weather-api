import os

from load_dotenv import load_dotenv
import requests

load_dotenv()

URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    payload_params = {
        "q": "Paris",
        "key": os.getenv("WEATHER_API_KEY"),
    }
    result = requests.get(URL, params=payload_params)
    data = result.json()
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['location']['localtime']} Weather: "
        f"{data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
