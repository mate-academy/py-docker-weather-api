import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = "https://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": api_key,
        "q": "Paris",
        "aqi": "no",
    }

    res = requests.get(base_url, params=params)
    return(res.json())


if __name__ == "__main__":
    get_weather()
