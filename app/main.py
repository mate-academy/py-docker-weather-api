import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris" # noqa
    response = requests.get(url).json()

    print("City: Paris")
    print(f"Temperature: {response['current']['temp_c']}°C") # noqa
    print(f"Condition: {response['current']['condition']['text']}") # noqa


if __name__ == "__main__":
    get_weather()
