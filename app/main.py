import os
from datetime import datetime
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    city_name = "Paris"

    if not api_key:
        print("Set API_KEY environment variable")
        return

    url = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": api_key,
        "q": city_name,
    }
    print("Performing request to Weather API for city Paris")

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        country = data["location"]["country"]
        city = data["location"]["name"]
        local_time_str = data["location"]["localtime"]

        try:
            dt_object = datetime.strptime(local_time_str, "%Y-%m-%d %H:%M")
            formatted_time = dt_object.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            formatted_time = local_time_str

        temp_celsius = data["current"]["temp_c"]
        weather_description = data["current"]["condition"]["text"]

        print(
            f"{city}/{country} {formatted_time} Weather: "
            f"{temp_celsius} Celsius, {weather_description}"
        )

    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_weather()
