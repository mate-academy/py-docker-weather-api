import requests
import os

URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"

def get_weather() -> None:
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        print("Please set WEATHER_API_KEY not key found")
        return

    query_params = {
        "key": api_key,
        "q": CITY,
    }
    response = requests.get(URL, params=query_params)
    data = response.json()

    temp_c = data["current"]["temp_c"]
    print(temp_c)


if __name__ == "__main__":
    get_weather()
