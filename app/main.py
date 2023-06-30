import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    filtering = "Paris"

    params = {
        "key": api_key,
        "q": filtering
    }

    weather_url = "http://api.weatherapi.com/v1/current.json"
    timezone_url = "http://api.weatherapi.com/v1/timezone.json"

    weather_response = requests.get(weather_url, params=params)
    if weather_response.status_code == 200:
        weather_data = weather_response.json()["current"]

        temperature = weather_data["temp_c"]
        condition = weather_data["condition"]["text"]

    timezone_response = requests.get(timezone_url, params=params)
    if timezone_response.status_code == 200:
        timezone_data = timezone_response.json()
        local_time = timezone_data["location"]["localtime"]
        city = timezone_data["location"]["name"]
        country = timezone_data["location"]["country"]

        print(f"Performin request to Weather API for city {city}...")
        print(f"{city}/{country} {local_time} "
              f"Weather: {temperature}, {condition}")


if __name__ == "__main__":
    get_weather()
