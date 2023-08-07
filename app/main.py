import os
import requests

CITY = "Paris"
API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    res = requests.get(
        url="https://api.weatherapi.com/v1/current.json",
        params={"key": "bf6d0683bda645ff87a143919230708", "q": CITY}
    )
    res = res.json()
    print(f"{res['location']['name']}/{res['location']['country']} "
          f"{res['location']['localtime']} Weather: {res['current']['temp_c']} Celsius, "
          f"{res['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
