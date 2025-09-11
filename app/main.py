import os

import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather() -> None:
    KEY = os.getenv("API_KEY")
    URL = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": KEY,
        "q": "Paris",
    }

    result = requests.get(URL, params=params)
    data = result.json()

    print(f"{data['location']['name']} - {data['current']['temp_c']}")


if __name__ == "__main__":
    get_weather()
