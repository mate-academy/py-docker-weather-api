import os
import requests

API_KEY = os.environ.get("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    try:
        response = requests.get(
            url=URL,
            params={
                "key": API_KEY,
                "q": CITY
            }
        )
        response.raise_for_status()
        data = response.json()

        temp_c = int(data["current"]["temp_c"])
        temp_f = int(data["current"]["temp_f"])
        feelslike_c = int(data["current"]["feelslike_c"])
        condition_text = data["current"]["condition"]["text"].lower()

        print(f"Greetings!\nI hasten to inform you that"
              f" outside the window {condition_text} in Paris.\n"
              f"The temperature is {temp_c} Celsius ({temp_f}F),"
              f" feels like {feelslike_c}. Enjoy your stay!")

    except requests.exceptions.HTTPError as error:
        print(f"An HTTP error occurred: {error}")


if __name__ == "__main__":
    get_weather()
