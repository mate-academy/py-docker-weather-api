import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather(key: str) -> None:
    params = {
        "key": key,
        "q": CITY,
    }
    response = requests.get(URL, params=params)
    weather = response.json()
    print(
        f"{weather['location']['name']}/{weather['location']['country']} "
        f"{weather['location']['localtime']} Weather: "
        f"{weather['current']['temp_c']} Celsius, "
        f"{weather['current']['condition']['text']}"
    )


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")
    if api_key:
        get_weather(api_key)
    else:
        print("API_KEY not found.")
