import os
import requests


REQUEST_URL = "http://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
FILTER = "Paris"


def get_weather() -> None:
    response = requests.get(
        REQUEST_URL,
        params={"key": API_KEY, "q": FILTER}
    ).json()

    city = response["location"]["name"]
    country = response["location"]["country"]
    date = response["location"]["localtime"]
    temperature = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(
        f"{city}/{country} {date} "
        f"Weather: {temperature} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
