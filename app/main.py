import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY environment variable is missing.")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Weather in {location}: {temp}°C, {condition}")
    else:
        print(f"Failed to fletch weather: {response.status_code}")


if __name__ == "__main__":
    get_weather()
