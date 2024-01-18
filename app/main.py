import os
import requests

API_URL = "https://api.weatherapi.com/v1/current.json?"
FILTERING = "Paris"


def get_weather(key, city) -> None | str:
    url = f"{API_URL}key={key}&q={FILTERING}"
    result = requests.get(url)

    return result.json() if result.status_code == 200 else None


def print_weather(info) -> None:
    city_name = info["location"]["name"]
    country_name = info["location"]["country"]
    date_time = info["location"]["localtime"]
    temperature_celsius = info["current"]["temp_c"]
    temperature_fahrenheit = info["current"]["temp_f"]
    weather = info["current"]["condition"]["text"]

    print(
        f"City: {city_name}({country_name}) {date_time} {temperature_celsius}°C ({temperature_fahrenheit}℉) {weather}")


if __name__ == "__main__":
    api_key = os.getenv("API_KEY")

    if api_key is None:
        print("Error: API Key is not provided")

    else:
        weather_info = get_weather(api_key, FILTERING)
        print_weather(weather_info)
