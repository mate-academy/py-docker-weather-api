import os
import requests


API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
key = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        API_URL,
        params={"key": key, "q": CITY}
    )

    data = response.json()

    print(f"Current weather in {data['location']['name']} is "
          f"{data['current']['temp_c']}°C")


if __name__ == "__main__":
    get_weather()
