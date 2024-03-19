import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/"
API_ENDPOINT = "current.json"


def get_weather(city: str) -> None:
    response = requests.get(
        URL + API_ENDPOINT,
        params={
            "key": API_KEY,
            "q": city
        }
    )
    weather = response.json()["current"]

    print(
        f"The weather in {city} is "
        f"{weather["condition"]["text"].lower()}"
    )
    print(f"Temperature in Celsius: {weather["temp_c"]}")
    print(f"Temperature in Fahrenheit: {weather["temp_f"]}")


if __name__ == "__main__":
    get_weather("Paris")
