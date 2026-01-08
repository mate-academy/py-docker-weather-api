import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data["location"]["name"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"{name}/current weather: {temp_c} Celsius, {condition}")
    else:
        print(f"Error fetching weather: {response.status_code}")


if __name__ == "__main__":
    get_weather()
