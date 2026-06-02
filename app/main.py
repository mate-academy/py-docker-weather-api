import os
import requests


API_KEY = os.getenv("WEATHER_API_KEY")
CITY = "Paris"
URL = "http://api.weatherapi.com/v1/current.json?"


def get_weather() -> None:
    if not API_KEY:
        print("Error: API KEY not found")
        return

    try:
        response = requests.get(URL + f"key={API_KEY}&q={CITY}")
        response.raise_for_status()
        data = response.json()
        city = data["location"]["name"]
        country = data["location"]["country"]
        data_time = data["current"]["last_updated"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(
            f"{city}/{country} {data_time} "
            f"Weather: {temp_c} Celsius, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"Error: url is not valid - {e}")


if __name__ == "__main__":
    get_weather()
