import os

import requests

URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.getenv("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    response = requests.get(URL, params={"key": API_KEY, "q": CITY}).json()
    location = (
        f"{response['location']['name']}\\{response['location']['country']}"
    )
    time = response["location"]["localtime"]
    weather = response["current"]["temp_c"]
    condition = response["current"]["condition"]["text"]

    print(
        f"Hello!\nToday in {location}\n"
        f"We have Weather like this: \n"
        f"{int(weather)} Celsius, "
        f"and {condition}\n"
        f"local time - {time}"
    )


if __name__ == "__main__":
    get_weather()
