import os
from requests import get


API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"
PARAMS = {
    "key": API_KEY,
    "q": CITY,
}


def get_weather() -> None:
    res = get(url=URL, params=PARAMS)

    if res.status_code == 200:
        weather_data = res.json()

        city_datetime = weather_data["location"]["localtime"]
        cur_temp = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        print(f"Current weather in {CITY} at {city_datetime}: \n"
              f"{cur_temp}°C \n"
              f"{condition}")


if __name__ == "__main__":
    get_weather()
