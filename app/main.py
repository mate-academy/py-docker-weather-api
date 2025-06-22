import requests
import os
import sys


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"
WEATHER_API_KEY = "API_KEY"
UNITS = "metric"


def get_weather() -> None:
    api_key = os.getenv(WEATHER_API_KEY)

    if not api_key:
        print(
            f"Error: {WEATHER_API_KEY} environment variable "
            f"not set. Please set it."
        )
        sys.exit(1)

    query_parameters = {
        "q": CITY,
        "key": api_key
    }

    try:
        response = requests.get(URL, params=query_parameters)
        response.raise_for_status()
        weather_data = response.json()
        if weather_data:
            city_name = weather_data["location"]["name"]
            country_name = weather_data["location"]["country"]
            localtime = weather_data["location"]["localtime"]
            temp_c = weather_data["current"]["temp_c"]
            condition = weather_data["current"]["condition"]["text"]
            print(
                f"{city_name}/{country_name} "
                f"{localtime} Weather: {temp_c}, {condition}"
            )
        else:
            print(f"Could not retrieve weather data for {CITY}.")
            sys.exit(1)

    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    get_weather()
