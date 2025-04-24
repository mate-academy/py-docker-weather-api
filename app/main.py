import os
import sys
import urllib.request
from urllib.error import HTTPError
import json


API_KEY = os.getenv("API_KEY")
if API_KEY is None or API_KEY == "":
    print("API_KEY was not set. Ensure you set this environment variable")
    sys.exit(1)
TYPE = "current.json"
APP_URL = "http://api.weatherapi.com/v1"
CITY = "Paris"
AQI = "no"
URL = f"{APP_URL}/{TYPE}?key={API_KEY}&q={CITY}&aqi={AQI}"


def get_weather() -> None:
    print(f"Performing request to Weather API for city {CITY}...")
    out_error = None
    try:
        with urllib.request.urlopen(URL) as response:
            content = response.read().decode("utf-8")
    except HTTPError as e:
        out_error = e
        content = e.fp.read().decode("utf-8")

    try:
        data = json.loads(content)
    except json.decoder.JSONDecodeError:
        print("JSON Decode Error. "
              "Probably got HTML because of response error.")
        print(out_error)
        return

    if out_error is not None:
        print(out_error)
        print(data)
        return

    location = data["location"]
    country = location["country"]

    current = data["current"]
    last_updated = current["last_updated"]
    temp_c = current["temp_c"]

    condition = current["condition"]
    condition_text = condition["text"]

    weather = f"Weather: {temp_c} Celsius, {condition_text}"
    result = f"{CITY}/{country} {last_updated} {weather}"

    print(result)


if __name__ == "__main__":
    get_weather()
