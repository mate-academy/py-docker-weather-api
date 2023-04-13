import os

import requests


def get_weather() -> None:
    url = "https://api.weatherapi.com/v1/current.json"
    api_key = os.environ.get("API_KEY")
    params = {
        "key": api_key,
        "q": "Paris",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        city = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        print(f"Current weather in {city}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")
    else:
        print("Failed to retrieve weather data.")


if __name__ == "__main__":
    get_weather()
