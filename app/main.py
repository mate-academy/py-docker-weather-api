import requests
import os


API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.weatherapi.com/v1/current.json"

params = {
    "key": API_KEY,
    "q": "Paris",
}


def get_weather() -> None:
    response = requests.get(BASE_URL, params)

    if response.status_code == 200:
        data = response.json()
        print(
            f"{data['location']['name']} {data['current']['last_updated']}"
            f" Weather: {data['current']['temp_c']} Celsius,"
            f" {data['current']['condition']['text']}")
    else:
        print(f"Failed to get weather data."
              f" Status code: {response.status_code}")


if __name__ == "__main__":
    get_weather()
