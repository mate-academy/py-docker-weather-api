import os
import requests

API_KEY = os.environ["API_KEY"]
CITY = "Paris"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    response = requests.get(
        BASE_URL,
        params={"key": API_KEY, "q": CITY}
    )
    data = response.json()

    location = data["location"]
    current = data["current"]

    city_name = location["name"]
    country = location["country"]
    localtime = location["localtime"]
    temp = current["temp_c"]
    condition = current["condition"]["text"]

    date, time = localtime.split(" ")

    print(
        f"{city_name}/{country} {date} {time}"
        f" Weather: {temp} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
