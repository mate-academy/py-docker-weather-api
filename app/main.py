import os
import requests


def get_weather(city):
    key = os.environ.get('API_KEY')
    response = requests.get("http://api.weatherapi.com/v1/current.json", params={
        "key": key,
        "q": city,
    })

    info = response.json()
    country = info["location"]["country"]
    current_city = info["location"]["name"]
    date = info["location"]["localtime"]
    weather = info["current"]["condition"]["text"]
    temperature = info["current"]["temp_c"]

    print(f"{current_city}, {country}\n{date}\n{temperature}°C, {weather}")


if __name__ == "__main__":
    city = "Paris"
    get_weather(city)
