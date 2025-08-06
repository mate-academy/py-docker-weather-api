import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise Exception("API_KEY not found in environment variables")

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key=" \
          f"{api_key}&q={city}&aqi=no"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Error fetching weather: {response.text}")

    data = response.json()
    location = data["location"]["name"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"Current weather in {location}: {temp_c}°C, {condition}")


if __name__ == "__main__":
    get_weather()
