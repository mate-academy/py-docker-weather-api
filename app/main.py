import os
import requests


API_KEY = os.getenv("API_KEY")
API_URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    if not API_KEY:
        raise ValueError("API_KEY environment variable not found!")

    params = {"key": API_KEY, "q": CITY}

    weather_data = requests.get(API_URL, params=params)
    weather_data.raise_for_status()
    weather_data = weather_data.json()

    loc_name = weather_data["location"]["name"]
    loc_country = weather_data["location"]["country"]
    loc_time = weather_data["location"]["localtime"]
    loc_temperature = weather_data["current"]["temp_c"]
    loc_weather = weather_data["current"]["condition"]["text"]

    weather_line = (
        f"{loc_country}/{loc_name} {loc_time} "
        f"Weather: {loc_temperature} Celsius, {loc_weather}"
    )

    print(weather_line)


if __name__ == "__main__":
    get_weather()
