import os
import requests


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"

API_KEY = os.getenv("API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": CITY,
            "aqi": "no",
        }
    )

    data = response.json()

    city_name = data["location"]["name"]
    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    weather_text = data["current"]["condition"]["text"]

    print(
        f"{city_name}/{country} {local_time} "
        f"Weather: {temp_c} Celsius, {weather_text}"
    )


if __name__ == "__main__":
    get_weather()
