import requests
import os


weather_site = "https://api.weatherapi.com/v1/current.json?key="


def get_weather() -> None:
    city = "Paris"
    api_key = os.environ["weatherapi_key"]
    url = f"{weather_site}{api_key}&q={city}&aqi=no"

    data = requests.get(url, params={"city": city})
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
