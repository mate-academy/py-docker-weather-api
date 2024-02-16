import os

import requests


def get_weather(location: str) -> None:
    request = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        {"key": os.getenv("WEATHER_API_KEY"), "q": location},
    )
    if request.status_code == 200:
        print_weather(request.json())
    else:
        print(f"Something wrong, status_code: {request.status_code}")


def print_weather(weather: dict) -> None:
    location = weather["location"]
    current_weather = weather["current"]

    print(f"""
    Country: {location['country']}
    City: {location['name']}
    TimeZone: {location['tz_id']}
    Time: {location['localtime']}
    {"-" * 22}
    Weather
    Temperature: {current_weather['temp_c']}
    Feels like: {current_weather['feelslike_c']}
    Part of day: {('Day', 'Night')[current_weather['is_day']]}
    Wind speed: {current_weather['wind_kph']}km/h
    Wind direction: {current_weather['wind_dir']}
    Humidity: {current_weather['humidity']}
    Cloud: {current_weather['cloud']}
    """)


if __name__ == "__main__":
    get_weather("Paris")
