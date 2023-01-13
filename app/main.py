import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_KEY"]
URL = "https://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"


def get_weather(api_key: str) -> None:
    try:
        result = requests.get(URL, params={"q": FILTERING, "key": api_key})
        data = result.json()
        print(
            f"{data['location']['name']}/{data['location']['country']} "
            f"{data['location']['localtime']} "
            f"Weather: {data['current']['temp_c']} Celsius, "
            f"{data['current']['condition']['text']}"
        )

    except Exception as e:
        print("Exception (weather):", e)


if __name__ == "__main__":
    get_weather(API_KEY)
