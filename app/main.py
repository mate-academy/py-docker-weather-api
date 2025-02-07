import os
import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = os.environ.get("CITY", "Paris")


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY environment variable is not set")

    response = requests.get(API_URL, params={"key": API_KEY, "q": CITY})

    if response.status_code == 200:
        data = response.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        localtime = data["location"]["localtime"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(
            f"{city}/{country} {localtime} "
            f"Weather: {temp} Celsius, {condition}"
        )
    else:
        print(
            f"Failed to get weather data: "
            f"{response.status_code}, {response.text}"
        )


if __name__ == "__main__":
    get_weather()
