import requests
import os


def get_weather() -> None:
    weatherapi = os.environ["weatherapi_key"]
    city_to_find = "Paris"

    url = f"https://api.weatherapi.com/v1/current.json?key=" \
          f"{weatherapi}&q={city_to_find}&aqi=no"
    data = requests.get(url)
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
