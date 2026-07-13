import os
import requests

BASE_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is not set")

    response = requests.get(f"{BASE_URL}?key={api_key}&q={CITY}")
    data = response.json()

    print(
        f"{data['location']['name']}/{data['location']['country']} "
        f"Weather: {data['current']['temp_c']}°C, "
        f"{data['current']['condition']['text']}"
    )


if __name__ == "__main__":
    get_weather()
