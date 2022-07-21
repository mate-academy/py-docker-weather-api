import os
import requests


def get_weather():
    city_name = "Paris"
    api_key = os.environ.get("API_KEY")
    params = {"key": api_key, "q": city_name}
    base_url = "http://api.weatherapi.com/v1/current.json"
    res = requests.get(base_url, params)
    data = res.json()

    city = data["location"]["tz_id"]
    date_time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    temperature_feels_like = data["current"]["feelslike_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Weather in {city} (date/time: {date_time}):\n"
          f"Temperature in Celsius: {temperature} "
          f"(feels like {temperature_feels_like})\n"
          f"Condition: {condition}")


if __name__ == "__main__":
    get_weather()
