import os
import requests

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    api_key = os.environ["API_KEY"]
    response = requests.get(URL, params={"key": api_key, "q": CITY})
    data = response.json()
    location = data["location"]
    current = data["current"]
    print(
        f"The current weather in {location['name']}, {location['country']}:\n"
        f"Temperature: {current['temp_c']}°C\n"
        f"Condition: {current['condition']['text']}\n"
        f"Wind: {current['wind_kph']} kph\n"
        f"Humidity: {current['humidity']}%"
    )


if __name__ == "__main__":
    get_weather()
