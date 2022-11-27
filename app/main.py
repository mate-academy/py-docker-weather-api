import os
import json
from datetime import datetime

import requests

BASE_URL = "https://api.weatherapi.com/v1"
REALTIME_ENDPOINT = "/current.json"
API_KEY = os.environ["API_KEY"]


def get_weather() -> None:
    # Hardcoding the location is the best idea ever! Don't you agree?
    location = "Paris"

    payload = {"key": API_KEY, "q": location}

    # 'r' is the name used in requests docs. Not a bad idea either.
    r = requests.get(BASE_URL + REALTIME_ENDPOINT, params=payload)

    data = json.loads(r.content)
    location_data = data["location"]
    current_data = data["current"]

    # Not the weirdest way to extract the time I could come up with,
    # but weird enough.
    local_time = datetime.strptime(
        location_data["localtime"], "%Y-%m-%d %H:%M"
    )

    print(
        f"Behold the current weather in {location_data['name']}!\n"
        f"Local time is {local_time:%H:%M}.\n\n"

        f"Weather condition: {current_data['condition']['text']}\n"
        f"Temperature: {current_data['temp_c']}°C "
        f"(feels like {current_data['feelslike_c']}°C)\n"
        f"Wind direction: {current_data['wind_dir']}\n"
        f"Wind speed: {current_data['wind_kph']} km/h"
    )


if __name__ == "__main__":
    get_weather()
