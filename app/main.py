import requests
import os

# 081126877d5248ee810191659221411
BASE_URL = "http://api.weatherapi.com/v1/current.json?key="
CITY = "Paris"
API_KEY = os.environ.get("API_KEY")


def full_url(base: str, key: str, city: str) -> str:
    return base + key + "&q=" + city + "&aqi=no"


def get_weather() -> None:
    api_result = requests.get(full_url(BASE_URL, API_KEY, CITY))
    if api_result.status_code == 200:
        api_response = api_result.json()
        for key, value in api_response.items():
            print(f"{key}: {value}")
    else:
        print("Error in the HTTP request")


if __name__ == "__main__":
    get_weather()
