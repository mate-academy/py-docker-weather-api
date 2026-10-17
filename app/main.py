import os
import requests

URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.getenv("API_KEY")

    params = {
        "key": api_key,
        "q": CITY,
    }
    response = requests.get(URL, params=params)
    response.raise_for_status()

    weather_data = response.json()

    print(
        f"{weather_data["location"]["name"]}: "
        f"{weather_data["current"]["temp_c"]}°C, "
        f"{weather_data["current"]["condition"]["text"]}"
    )


if __name__ == "__main__":
    get_weather()
