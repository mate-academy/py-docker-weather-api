import os
import requests


def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    CITY = "Paris"
    BASE_URL = "https://api.weatherapi.com/v1/current.json"
    url = f"{BASE_URL}?q={CITY}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    country = data["location"]["country"]
    local_time = data["location"]["localtime"]
    temperature = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    results = f"{CITY}/{country} {local_time} Weather: {temperature} Celsius, {condition}"
    print (results)


if __name__ == "__main__":
    get_weather()
