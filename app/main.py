import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")

    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": "Paris",
        "aqi": "no"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    weather_info = data["current"]

    temperature = weather_info["temp_c"]
    condition = weather_info["condition"]["text"]
    wind = weather_info["wind_kph"]
    humidity = weather_info["humidity"]

    print("Current weather in Paris:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Wind: {wind} kph")
    print(f"Humidity: {humidity}%")


if __name__ == "__main__":
    get_weather()
