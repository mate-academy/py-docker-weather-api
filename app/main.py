import os
import requests


def get_weather() -> None:
    print("Perfoming request to Weather API for city Paris...")
    api_key = os.getenv("API_KEY")
    URL = "http://api.weatherapi.com/v1/current.json?"
    FILTERING = "Paris"
    weather = requests.get(URL + f"key={api_key}&q={FILTERING}&aqi=no").json()
    print(f"{weather['location']['name']}/"
          f"{weather['location']['country']} "
          f"{weather['location']['localtime']} "
          f"Weather: {weather['current']['temp_c']} Celsius, "
          f"{weather['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
