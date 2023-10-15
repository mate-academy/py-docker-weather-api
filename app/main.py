import os
import requests
from dotenv import load_dotenv


load_dotenv()
URL = "http://api.weatherapi.com/v1/current.json"
FILTER = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    payload = {
        "key": API_KEY,
        "q": FILTER,
    }

    response = requests.get(URL, params=payload)

    if response.status_code != 200:
        print(f"No data: error code {response.status_code}")
        return

    data = response.json()

    print(
        f"Perfoming request to Weather API for city "
        f"{data['location']['name']}..."
    )
    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"{data['current']['last_updated']} "
        f"Weather: {data['current']['temp_c']} Celcius, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
