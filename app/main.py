import requests
import os


weather_site = "https://api.weatherapi.com"


def get_weather() -> None:
    FILTERING = "Paris"
    api_key = os.environ["weatherapi_key"]
    URL = f"{weather_site}/v1/current.json?key={api_key}"

    data = requests.get(f"{URL}&q={FILTERING}")
    data = data.json()
    city = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temp_c"]
    weather = data["current"]["condition"]["text"]
    local_time = data["location"]["localtime"]

    print(f"{city}/{country} {local_time} "
          f"Weather: {temperature} Celsius, {weather}")


if __name__ == "__main__":
    get_weather()
