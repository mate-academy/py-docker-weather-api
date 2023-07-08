import os
import requests


def get_weather() -> None:
    response = requests.get(URL)
    data = response.json()

    current = data.get("current")
    date = current.get("last_updated")
    temperature = current.get("temp_c")
    condition = current.get("condition").get("text")

    print(f"Paris/France {date} Weather: {temperature} Celsius, {condition}")


if __name__ == "__main__":

    API_KEY = os.environ.get("API_KEY")
    FILTERING = "Paris"
    URL = f"http://api.weatherapi.com/v1/current.json?key=" \
          f"{API_KEY}&q={FILTERING}&aqi=no"
    get_weather()
