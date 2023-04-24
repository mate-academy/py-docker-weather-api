import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(
        url=URL,
        params={
            "key": API_KEY,
            "q": CITY
        }
    ).json()

    temp_c = int(response["current"]["temp_c"])
    temp_f = int(response["current"]["temp_f"])
    feelslike_c = int(response["current"]["feelslike_c"])
    condition_text = response["current"]["condition"]["text"].lower()

    print(f"Greetings!\nI hasten to inform you that"
          f" outside the window {condition_text} in Paris.\n"
          f"The temperature is {temp_c} Celsius ({temp_f}F),"
          f" feels like {feelslike_c}. Enjoy your stay!")


if __name__ == "__main__":
    get_weather()
