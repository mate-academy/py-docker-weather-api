import os

import requests


def get_weather() -> None:
    """Get weather data from an external API and print the result."""
    api_key = os.environ.get("WEATHER_API_KEY")
    url = ("http://api.weatherapi.com/v1/current.json?"
           f"key={api_key}&q=Paris&lang=en")

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.reason}")
    else:
        data = response.json()

        location = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"The weather in {location} is {temperature}°C and {condition}")


if __name__ == "__main__":
    get_weather()
