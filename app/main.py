import os
import requests

def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY is not set")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q=Paris"
    response = requests.get(url)
    data = response.json()

    city = data["location"]["name"]
    country = data["location"]["country"]
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(f"{city}/{country} Weather: {temp}°C, {condition}")

if __name__ == "__main__":
    get_weather()
