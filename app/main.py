import os

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
        localtime = data["location"]["localtime"]
        temp_c = data["current"]["temp_c"]
        last_updated = data["current"]["last_updated"]
        weather = data["current"]["condition"]["text"]
        print(
            f"Today in {city} {weather.lower()}"
            f" at {localtime.hour}:{localtime.minute}. "
            f"Temperature is {int(temp_c)} Celsius degrees.\n"
            f"Weather for {region} region "
            f"was updated at {last_updated.hour}:{last_updated.minute}"
        )
    else:
        error = data["error"]["message"]
        print(
            f"Ooops, something goes wrong. "
            f"Seems like {error}"
        )


if __name__ == "__main__":
    get_weather()
