import requests
import os

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL,
        params={"aqi": "no", "q": CITY, "key": API_KEY}
    ).json()
    city = response["location"]["name"]
    country = response["location"]["country"]
    localtime = response["location"]["localtime"]
    temp = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(
        f"{city}/{country} {localtime} Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
