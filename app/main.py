import requests
import os

KEY = os.environ["API_KEY"]
BASE_URL = "http://api.weatherapi.com/v1"
FILTERING = "Paris"


def get_weather() -> None:
    response = requests.get(
        f"{BASE_URL}/current.json",
        params={
            "key": KEY,
            "q": FILTERING
        }
    )
    data = response.json()
    print(f"Performing request for to weather API for city of {FILTERING}...")
    print(
        f"{data['location']['localtime']}"
        f" Weather: {data['current']['temp_c']} Celsius, "
        f"{data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
