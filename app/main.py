import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        URL, params={"key": API_KEY, "q": CITY}
    )
    weather = response.json()["current"]

    print(
        f"The weather in {CITY} is "
        f"{weather["condition"]["text"].lower()}"
    )
    print(f"Temperature in Celsius: {weather["temp_c"]}")
    print(f"Temperature in Fahrenheit: {weather["temp_f"]}")


if __name__ == "__main__":
    get_weather()
