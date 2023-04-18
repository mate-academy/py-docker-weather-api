import os
import requests

URL = "https://api.weatherapi.com/v1/current.json?"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    response = requests.get(
        URL + f"key={api_key}" + f"&q={CITY}" + "&aqi=no"
    )
    weather_data_dict = response.json()
    location_data = weather_data_dict.get("location")
    temperature_data = weather_data_dict.get("current")
    condition_data = temperature_data.get("condition")
    result = (
        f"{location_data['name']}/{location_data['country']} "
        f"{location_data['localtime']} "
        f"Weather: {temperature_data['temp_c']} "
        f"Celsius, {condition_data['text']}"
    )
    print(f"Performing request to Weather API for city {CITY}...")
    print(result)


if __name__ == "__main__":
    get_weather()
