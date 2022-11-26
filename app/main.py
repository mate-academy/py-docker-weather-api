import os
import requests

BASE_URL = "https://api.weatherapi.com/v1/current.json?"
CITY_NAME = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    try:
        response = requests.get(BASE_URL, {"key": API_KEY, "q": CITY_NAME})
    except requests.exceptions.ConnectionError:
        print("Please, check your internet connection!")
    else:
        data = response.json()
        city = data["location"]["name"]
        condition = data["current"]["condition"]["text"].casefold()
        temp_c = int(data["current"]["temp_c"])

        if response.status_code == 200:
            print(
                f"It is {condition} in {city} "
                f"temperature is {temp_c} Celsius degrees"
            )
        else:
            print(
                f"Something go wrong! HTTP Status Code: {response.status_code}"
            )


if __name__ == "__main__":
    get_weather()
