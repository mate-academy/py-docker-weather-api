import os
import requests


def get_weather() -> None:
    params = {"q": "Paris", "key": os.environ["API_KEY"]}
    response = requests.get(
        "https://api.weatherapi.com/v1/current.json",
        params=params
    )
    data = response.json()
    print(f"{data['location']['name']} "
          f"{data['location']['localtime']} "
          f"Weather {data['current']['temp_c']} "
          f"Celsius - {data['current']['condition']['text']}")


if __name__ == "__main__":
    get_weather()
