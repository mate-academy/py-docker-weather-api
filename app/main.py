import os
import requests

CITY = "Paris"
API_KEY = os.environ["API_KEY"]
URL = "http://api.weatherapi.com/v1/current.json"

def get_weather() -> None:
    params = {"q": CITY, "key": API_KEY}
    response = requests.get(
        URL,
        params=params
    )
    data = response.json()
    print(f"{data['location']['name']} "
          f"{data['location']['localtime']} "
          f"Weather {data['current']['temp_c']} "
          f"Celsius - {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
