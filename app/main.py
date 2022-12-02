import os
import requests

API_URL = "https://api.weatherapi.com/v1/current.json"
API_KEY = os.environ.get("API_KEY")
CITY = "Paris"


def get_weather() -> None:
    res = requests.get(f"{API_URL}?key={API_KEY}&q={CITY}").json()

    city = res["location"]["name"]
    county = res["location"]["country"]
    time = res["location"]["localtime"]
    temp_c = res["current"]["temp_c"]
    feelslike_c = res["current"]["feelslike_c"]
    condition = res["current"]["condition"]["text"].lower()
    wind_kmp = res["current"]["wind_kph"]
    wind_dir = res["current"]["wind_dir"]
    print(
        f"In {city}({county}) today {condition} and {temp_c} "
        f"degrees Celsius, feels like {feelslike_c} degrees.\n"
        f"Also {wind_dir} wind with speed {wind_kmp} km/h."
        f"Current time {time}.\n"
        "Have a good day."
    )


if __name__ == "__main__":
    get_weather()
