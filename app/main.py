import requests
import os


URL = "https://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    print(f"Performing request to Weather API for {CITY}...")
    api_key = os.getenv("API_KEY")
    payload = {"key": api_key, "q": CITY}
    response = requests.get(URL, params=payload)
    location = response.json()["location"]
    data = response.json()["current"]
    weather = (f"{location['name']}/{location['country']} "
               f"{data['last_updated']} Weather: {data['temp_c']} Celsius, "
               f"{data['condition']['text']}")
    print(weather)


if __name__ == "__main__":
    get_weather()
