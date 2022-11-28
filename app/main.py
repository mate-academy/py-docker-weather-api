import requests
import os

BASE_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(BASE_URL, params={"key": API_KEY, "q": CITY})
    info = response.json()
    print(info)
    if response.status_code == 200:
        city = info["location"]["name"]
        date = info["location"]["localtime"]
        temp = info["current"]["temp_c"]
        condition = info["current"]["condition"]["text"]

        print(
            f"Today on {date} the weather in {city}:"
            f"Temperature: {temp} Celsius"
            f"Condition: {condition}"
        )

    else:
        print("Something went wrong...")


if __name__ == "__main__":
    get_weather()
