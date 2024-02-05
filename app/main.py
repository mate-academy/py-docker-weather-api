import requests
import os


def get_weather() -> None:
    req = requests.get(f"http://api.weatherapi.com/v1/current.json?"
                       f"key={os.getenv('API_KEY')}&q=Paris&aqi=yes")
    if req.status_code == 200:
        print("Performing request to Weather API for city Paris...")
        print(f"Paris/France"
              f" {req.json().get('location')['localtime']}"
              f" Weather: {req.json().get('current').get('temp_c')}"
              f" Celsius, {req.json().get('current').get('condition').get('text')}"
              )


if __name__ == "__main__":
    get_weather()
