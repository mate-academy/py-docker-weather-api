import os
from datetime import datetime

import requests

URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    response = requests.get(URL, {"key": API_KEY, "q": FILTERING})
    data = response.json()

    if response.status_code == 200:
        city = data["location"]["name"]
        region = data["location"]["region"]
        localtime = datetime.strptime(
            data["location"]["localtime"], "%Y-%m-%d %H:%M"
        )
        temp_c = data["current"]["temp_c"]
        last_updated = datetime.strptime(
            data["current"]["last_updated"], "%Y-%m-%d %H:%M"
        )
        weather = data["current"]["condition"]["text"]
        print(
            f"Today in {city} {weather.lower()}"
            f" at {localtime.hour}:{localtime.minute}. "
            f"Temperature is {int(temp_c)} Celsius degrees.\n"
            f"Weather for {region} region "
            f"was updated at {last_updated.hour}:{last_updated.minute}"
        )
    else:
        print(
            f"Ooops, something goes wrong. "
            f"Seems like {data['error']['message']}"
        )


if __name__ == "__main__":
    get_weather()
