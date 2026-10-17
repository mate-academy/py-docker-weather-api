import os
import requests


def get_weather() -> None:
    print("Perfoming request to Weather API for city Paris...")
    api_key = os.getenv("API_KEY")
    URL = "http://api.weatherapi.com/v1/current.json?"
    FILTERING = "Paris"
    x = requests.get(URL + f"key={api_key}&q={FILTERING}&aqi=no").json()
    print(f"{x['location']['name']}/"
          f"{x['location']['country']} "
          f"{x['location']['localtime']} "
          f"Weather: {x['current']['temp_c']} Celsius, "
          f"{x['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
