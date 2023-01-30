import requests
import os


API_KEY = os.environ["weatherapi_key"]
URL = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}"

FILTERING = "Paris"


def get_weather() -> None:
    data = requests.get(URL, params={"q": FILTERING})
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
