import os
import requests


URL = "http://api.weatherapi.com/v1/current.json"
FILTERING = "Paris"
API_KEY = os.environ.get("WEATHER_API_KEY")


def get_weather() -> None:
    response = requests.get(
        URL,
        params={
            "key": API_KEY,
            "q": FILTERING,
        }
    )
    if response.status_code == 200:
        data = response.json()
        print(f"Performing request to Weather API for city "
              f"{data['location']['name']}")
        print(
            f"{data['location']['localtime']}, "
            f"{data['location']['name']}, {data['location']['country']}\n"
            f"current temperature: {data['current']['temp_c']}C"
            f"{data['current']['condition']['text']}"
        )
    else:
        print(
            f"Failed to retrieve weather data. "
            f"Status Code: {response.status_code}"
        )


if __name__ == "__main__":
    get_weather()
