import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    if not API_KEY:
        print("No api key provided")
        return
    payload = {"q": "Paris", "key": API_KEY}
    res = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params=payload
    )
    print(res.text)


if __name__ == "__main__":
    get_weather()
