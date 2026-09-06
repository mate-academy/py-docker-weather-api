import os
import requests

API_KEY = os.environ.get("API_KEY")
WEATHER_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        print("API key not provided")
        return
    response = requests.get(WEATHER_URL + f"?q={CITY}&key=" + API_KEY)
    if response.status_code == 200:
        data = response.json()
        current_weather = data["current"]["condition"]["text"]
        local_time = data["location"]["localtime"]
        current_temp = data["current"]["temp_c"]
        result = (f"It's {current_weather} ({current_temp} °C) "
                  f"in {CITY} at the {local_time} local time")
        print(result)


if __name__ == "__main__":
    get_weather()
